<?php
include 'db.php';

$search = isset($_GET['search']) ? $_GET['search'] : '';

$conn = getDbConnection();
$query = "SELECT * FROM products WHERE name LIKE '%$search%'";  // SQL Injection vulnerability
$result = $conn->query($query);

echo "<h1>Search Results</h1>";
while ($row = $result->fetch_assoc()) {
    echo $row['name'] . ": " . $row['content'] . "<br>";
}

$conn->close();
?>
<form method="GET" action="search.php">
    <input type="text" name="search" placeholder="Search for products">
    <input type="submit" value="Search">
</form>
