<?php

$database = "jym";
$conn = new mysqli("localhost", "root", "", $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$sql = "CREATE TABLE student (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    email VARCHAR(50)
)";
$result = $conn->query($sql);

if ($result === TRUE) {
    echo "Table 'student' created successfully.";
} else {
    echo "Couldn't create table.";
}

$conn->close();
?>
