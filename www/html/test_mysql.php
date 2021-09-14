<?php
# Fill our vars and run on cli
# $ php -f db-connect-test.php

$dbname = 'remi';
$dbuser = 'remi';
$dbpass = 'Rime!000';
$dbhost = '127.0.0.1';

$link = mysqli_connect($dbhost, $dbuser, $dbpass) or die("Unable to Connect to '$dbhost'");
mysqli_select_db($link, $dbname) or die("Could not open the db '$dbname'");

$test_query = "SHOW TABLES FROM $dbname";
$result = mysqli_query($link, $test_query);

$tblCnt = 0;
while($tbl = mysqli_fetch_array($result)) {
  $tblCnt++;
  #echo $tbl[0]."<br />\n";
}

echo "With $dbuser user, in the $dbname database, ";
if (!$tblCnt) {
  echo "there are no tables<br />\n";
} else {
  echo "there are $tblCnt tables<br />\n";
}

?>

