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
$var7= $userRow1['DeptNo'];
$res2=mysql_query("SELECT * FROM Departments WHERE DeptNo=$var7");
$userRow2=mysql_fetch_array($res2);

?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Welcome - <?php echo $userRow['Firstname']; ?></title>
<link rel="stylesheet" href="style.css" type="text/css" />
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

<div id="body">
     <div id="lineLeft">
  <?php  $var1= $userRow['FirstName'];
    $var2= $userRow1['MidInit'];
    $var3= $userRow1['LastName'];
    $var4= $userRow1['RollNo'];
    $var5= $userRow1['Semester'];
    $var6= $userRow1['YearEnrolled'];
    $var8= $userRow2['deptname'];



   ?>
    <h2>Student Details </h2><br/>
    Roll Number : <?php echo "$var4 "; ?> 
    <br/>
	Name : <?php echo "$var1 $var2 $var3"; ?>
    <br/>
    Department Name : <?php echo "$var8 "; ?>
    <br/>
    Semester : <?php echo "$var5 "; ?>
    <br/>
    Year Enrolled : <?php echo "$var6 "; ?>
      </div>
   <div id="lineRight">
      <h2>Course Registration</h2><br/> 
      <a href='coursereg.php'>Click Here For Course Registration</a>
      

    </div>
   <div id="lineRight2">
      <h2>Change Password</h2><br/> 
      <a href='password.php'>Change Password</a>
      

    </div>

</div>

</body>
</html>