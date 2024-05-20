<?php
include 'db.php';

$conn = getDbConnection();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $comment = $_POST['comment'];
    $query = "INSERT INTO comments (comment) VALUES ('$comment')";  // XSS vulnerability
    $conn->query($query);
}

$result = $conn->query("SELECT * FROM comments");
echo "<h1>Comments</h1>";
while ($row = $result->fetch_assoc()) {
    echo $row['comment'] . "<br>";  // Displaying unsanitized user input
}

$conn->close();
?>
<form method="POST" action="xss.php">
    <input type="text" name="comment" placeholder="Enter your comment">
    <input type="submit" value="Submit">
</form>
