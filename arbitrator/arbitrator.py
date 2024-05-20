from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

SERVERS = [
    "http://s1:80",
    "http://s2:80",
    "http://s3:80"
]

WAF_URL = "http://waf:80"
WAF_RULE_URL = "http://waf:9090"

class Arbitrator:
    @staticmethod
    def is_attack_detected(responses):
        # So sánh các phần nội dung chính (body) của phản hồi từ các máy chủ khác nhau
        bodies = [response.text for response in responses]
        for i in range(len(bodies) - 1):
            for j in range(i + 1, len(bodies)):
                if bodies[i] != bodies[j]:
                    return True
        return False

    @staticmethod
    def send_response_with_error():
        return "Error: Attack detected", 403

    @staticmethod
    def create_waf_rule(detected_pattern):
        print(f"Creating WAF rule to block detected pattern: {detected_pattern}")
        waf_rule = f'SecRule ARGS "{detected_pattern}" "deny,status:403,id:1000,msg:\'Detected Attack Pattern\'"\n'
        response = requests.post(WAF_RULE_URL, data=waf_rule.encode('utf-8'))
        if response.status_code == 200:
            print("WAF rule successfully created and applied.")
        else:
            print("Failed to create WAF rule.")

    @staticmethod
    def detect_attack_pattern(responses):
        # Phát hiện mẫu tấn công từ các phản hồi
        attack_patterns = ["UNION SELECT", "<script>", "DROP TABLE", "OR '1'='1"]
        bodies = [response.text for response in responses]
        for pattern in attack_patterns:
            for body in bodies:
                if pattern in body:
                    return pattern
        return None

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy(path):
    global WAF_URL, SERVERS

    method = request.method
    data = request.get_data()
    headers = {key: value for key, value in request.headers if key != 'Host'}

    waf_response = requests.request(method, f"{WAF_URL}/{path}", headers=headers, data=data, params=request.args)

    if waf_response.status_code == 403:
        return waf_response.text, 403

    selected_servers = random.sample(SERVERS, 3)
    responses = [waf_response]

    for server in selected_servers:
        response = requests.request(method, f"{server}/{path}", headers=headers, data=data, params=request.args)
        responses.append(response)

    if Arbitrator.is_attack_detected(responses):
        detected_pattern = Arbitrator.detect_attack_pattern(responses)
        if detected_pattern:
            Arbitrator.create_waf_rule(detected_pattern)
        return Arbitrator.send_response_with_error()
    else:
        return random.choice([response.text for response in responses])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
