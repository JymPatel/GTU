<?php

$database = "diet";
$conn = new mysqli("localhost", "root", "", $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SHOW TABLES";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo $row["Tables_in_" . $database] . "<br>";
    }
} else {
    echo "No tables found.";
}

$conn->close();
?>
