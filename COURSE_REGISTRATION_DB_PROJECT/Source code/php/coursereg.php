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
$var5= $userRow1['Semester'];
$var6= $userRow1['RollNo'];
$var7= $userRow1['DeptNo'];
$query="SELECT * FROM courses WHERE DeptNO=$var7 and Semester = $var5";
$result=mysql_query($query);
$num=mysql_numrows($result);

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
<div>
 <h2> <a href="home.php"><= Home</a> </h2>
  </div>

<div id="body">
  <center><h2>Course Registration</h2><br/></center>
 
  <h3>Course Details :</h3><br/>
 
Sl.No.
&nbsp
Enroll  
&nbsp &nbsp
Course Code    
&nbsp &nbsp    
Credits   &nbsp &nbsp      
Semester  &nbsp &nbsp   
Course Type &nbsp &nbsp 
Instructor Id    &nbsp &nbsp &nbsp &nbsp   
Course Name
<br/><br/>
<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">
  <?php
$i=0;while ($i < $num) { 
$f1=mysql_result($result,$i,"CourseCode");
$f2=mysql_result($result,$i,"CourseName");
$f3=mysql_result($result,$i,"Credits");
$f4=mysql_result($result,$i,"Semester");
$f5=mysql_result($result,$i,"InstructorID");
$f6=mysql_result($result,$i,"CourseType");
$j=$i+1;
echo " &nbsp ". $j. " &nbsp &nbsp &nbsp &nbsp &nbsp "
."<input type='checkbox' name='formSelect[]' value='$f1' />"
."  &nbsp &nbsp &nbsp &nbsp &nbsp "
. $f1 
. " &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp " 
. $f3. " &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp " 
. $f4. " &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp   " 
.$f6. " &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  " 
. $f5. " &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp "
. $f2."<br>";

$i++;}
?>
<br/><br/> 
<input type="submit" name="formSubmit" value="Submit" />
<br/><br/>    
C - CORE
<br/><br/> 
E - ELECTIVE
<br/><br/> 

<?php

  if(isset($_POST['formSubmit'])) 
    {
    $aArray = $_POST['formSelect'];
    
    
    
    if(empty($aArray)) 
        {
      echo("<p>You didn't select any Courses.</p>\n");
    } 
        else 
        {
            $N = count($aArray);
       $servername = "localhost";
       $username = "root";
       $password = "";
       $dbname = "course_reg";
       $conn = new mysqli($servername, $username, $password, $dbname);
       if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
      for($i=0; $i < $N; $i++)
      {
      
       
         $sql1= "INSERT INTO enrolled_on (RollNo,CourseCode)
        VALUES ($var6,'$aArray[$i]')";
        $var9=$aArray[$i];
      
      if ($conn->query($sql1) === TRUE) {
    echo "You have enrolled to " .$var9. " successfully";
} else {
    echo "Error: " . $sql1 . "<br>" . $conn->error;
}
      echo("</p>");
    }
      }  
        
        
  }
    
?>



   
</div>



</body>
</html>