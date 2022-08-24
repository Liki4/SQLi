<?php

ini_set("display_errors", "On");
error_reporting(E_ALL);

$conn = new mysqli("127.0.0.1","root","TjsDgwGPz5ANbJUU","sqli", 5738);
if ($conn -> connect_errno) {
    echo "Failed to connect to MySQL: " . $conn -> connect_error;
    exit();
}

$username=$_GET['username'];
$sql = "select * from users where username = '$username';";
echo $sql."<br>";
$conn->multi_query($sql);
$result = $conn->store_result();

if($result && $result->num_rows > 0){
    while ($row = $result->fetch_assoc()){
        echo "username: " . $row['username'] . "<br>";
        echo "password: " . $row['password'] . "<br>";
    }
}else{
    echo "failed:";
    echo $conn->error;
}

?>
