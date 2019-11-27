<?php
session_start();
include_once 'dbconnect.php';

if(!isset($_SESSION['user']))
{
	header("Location: index.php");
}
$res=mysql_query("SELECT * FROM admin WHERE UserName=".$_SESSION['user']);
$res1=mysql_query("SELECT * FROM Students WHERE RollNo=".$_SESSION['user']);
$userRow=mysql_fetch_array($res);
$userRow1=mysql_fetch_array($res1);

$conn = mysql_connect("localhost","root","");
mysql_select_db("phppot_examples",$conn);
if(count($_POST)>0) {
$result = mysql_query("SELECT * from admin WHERE UserName=".$_SESSION['user']);
$row=mysql_fetch_array($result);
if($_POST["currentPassword"] == $row["Password"]) {
mysql_query("UPDATE admin set Password='" . $_POST["newPassword"] . "' WHERE UserName='" . $_SESSION["user"] . "'");
$message = "Password Changed";
} else $message = "Current Password is not correct";
}

?>




<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Welcome - <?php echo $userRow['Firstname']; ?></title>
<link rel="stylesheet" href="style.css" type="text/css" />

<script>
function validatePassword() {
var currentPassword,newPassword,confirmPassword,output = true;

currentPassword = document.frmChange.currentPassword;
newPassword = document.frmChange.newPassword;
confirmPassword = document.frmChange.confirmPassword;

if(!currentPassword.value) {
  currentPassword.focus();
  document.getElementById("currentPassword").innerHTML = "required";
  output = false;
}
else if(!newPassword.value) {
  newPassword.focus();
  document.getElementById("newPassword").innerHTML = "required";
  output = false;
}
else if(!confirmPassword.value) {
  confirmPassword.focus();
  document.getElementById("confirmPassword").innerHTML = "required";
  output = false;
}
if(newPassword.value != confirmPassword.value) {
  newPassword.value="";
  confirmPassword.value="";
  newPassword.focus();
  document.getElementById("confirmPassword").innerHTML = "Passwords do not match";
  output = false;
}   
return output;
}
</script>

</head>
<body >
<div id="header">
	<div id="left">
    <label>NITK</label>
    </div>
    <div id="right">
    	<div id="content">
        	Welcome <?php echo $userRow['FirstName']; ?>!      &nbsp;<a href="logout.php?logout">Sign Out</a>
        </div>
    </div>

</div>
<div>
 <h2> <a href="home.php">< Home</a> </h2>
  </div>



     
  <center>

<div id="login-form">
<form name="frmChange" method="post"  action="" onSubmit="return validatePassword()">
  <div class="message"><?php if(isset($message)) { echo $message; } ?></div>
<table align="center" width="30%" border="0">
<tr>
<td><input type="password" name="currentPassword" placeholder="Your Old Password" class="txtField"/><span id="currentPassword"  class="required"></span></td>
</tr>

<tr>
<td><input type="password" name="newPassword" placeholder="Your New Password" class="txtField"/><span id="newPassword" class="required"></span></td>
</tr>

<td><input type="password" name="confirmPassword" placeholder="Confirm New Password" class="txtField"/><span id="confirmPassword" class="required"></span></td>
</tr>


<tr>
<td><button type="submit" name="submit" value="Submit" class="btnSubmit">Submit</button></td>
</tr>
</table>
</form>
</div>
</center>



</body>
</html>