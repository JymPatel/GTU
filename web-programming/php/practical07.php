<?php

$database = "jym";
$conn = new mysqli("localhost", "root", "", $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "ALTER TABLE student ADD COLUMN semester INT;";

$result = $conn->query($sql);

if ($result === TRUE) {
    echo "new column 'semester' added.";
} else {
    echo "Couldn't modify table.";
}

$conn->close();
?>
