<?php
$server_name = getenv('SERVER_NAME');
echo "Hello from $server_name!<br>";
?>
<a href="search.php">Search Products</a><br>
<a href="xss.php">Submit Comment</a><br>
<a href="xxe.php">Upload XML</a>
