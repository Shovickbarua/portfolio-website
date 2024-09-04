<?php
// Database connection details
$host = 'localhost';
$db = 'api_demo';
$user = 'root';
$password = '';

// Create connection
$conn = new mysqli($host, $user, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the input from form
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $message = $conn->real_escape_string($_POST['message']);

    // Validate input
    if (empty($name) || empty($email) || empty($message)) {
        echo "Name, email, and message are required";
        exit();
    }

    // Insert into database
    $sql = "INSERT INTO users (name, email, message) VALUES ('$name', '$email', '$message')";
    if ($conn->query($sql) === TRUE) {
        echo "Data submitted successfully";

        // Email details
        $to = 'shovickbarua92@gmail.com'; // Replace with your email address
        $subject = 'New Form Submission';
        $body = "You have received a new submission from your form:\n\n".
                "Name: $name\n".
                "Email: $email\n".
                "Message: $message\n";
        $headers = "From: noreply@example.com"; // Replace with a valid from address

        // Send the email
        if (mail($to, $subject, $body, $headers)) {
            echo " and an email notification has been sent.";
        } else {
            echo " but failed to send email notification.";
        }
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    // If not POST request, show an error
    echo "Invalid request method";
}

// Close connection
$conn->close();
?>
