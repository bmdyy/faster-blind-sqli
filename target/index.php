<?PHP
// William Moody (@bmdyy)
// 30.11.2022

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $conn = new mysqli("localhost", "kali", "kali", "fbsqli");
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT email FROM users WHERE username = '" . $_POST['username'] . "'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<b>Email was sent! If you don't see it in your inbox within 3 minutes, check your spam folder.</b><br>";
    } else {
        echo "<b>User " . htmlentities($_POST['username']) . " does not exist.</b><br>";
    }
    $conn->close();
    echo "Click <a href='/index.php'>here</a> to return";
    die();
}
?>

<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Faster Blind SQLi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>

<body>
    <nav class="navbar navbar-light bg-light px-2">
        <a class="navbar-brand" href="#">Faster (Boolean) Blind SQLi</a>
    </nav>
    <div class="container">
        <h3 class="mt-2">Reset Password</h3>
        <form method="POST" action="/index.php">
            <div class="form-group mb-2">
                <label for="usernameInput">Username</label>
                <input type="text" class="form-control" id="usernameInput" name="username" aria-describedby="usernameHelp" placeholder="Enter username">
                <small id="usernameHelp" class="form-text text-muted">Enter your username and we will send you an email with a password reset link.</small>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>