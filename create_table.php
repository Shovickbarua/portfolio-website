<?php
// Database connection details
$host = 'localhost';      // Database host
$db = 'api_demo';         // Database name
$user = 'root';           // Database username
$password = '';           // Database password

// Create connection
$conn = new mysqli($host, $user, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL to create table
$tableName = 'users';
$sql = "CREATE TABLE IF NOT EXISTS $tableName (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

// Execute the query
if ($conn->query($sql) === TRUE) {
    echo "Table '$tableName' created successfully.";
} else {
    echo "Error creating table: " . $conn->error;
}

// Close connection
$conn->close();
?>
