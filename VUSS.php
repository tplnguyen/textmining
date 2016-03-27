<?php
$search = $_POST['search'];
$text = file_get_contents('output.txt');
$lines = ($text . "\r\n");
$str = strstr($text, $_POST['search']);
if ($str == false){
  echo "Sorry! The email address for $search is not in this database.";
} else {
  echo "The email address of $search is in our database.<BR><BR> $lines";
}

/*$search = $_POST['search'];
$text = file_get_contents('output2.txt');
$lines = explode("\n", $text);
if(in_array($_POST['search'], $lines)){ //checks if address is in array
    echo "Mail was found";
}else{
    echo "I'm sorry. This staff member's email address in not in our database.";
}

$pos = strstr($array, $_POST['search']);
if ($pos == false){
  echo "The string '$search' was not found.";
} else{
  echo "'$array'";
}
$search = $_POST[$search];
$array = array(
  'emiel' => 'emiel.van.miltenburg@vu.nl',
  'lora' => 'lora.aroya@vu.nl');

  for ($i = 0; $i < count($array); $i++) {
    $key=key($array);
    $val=$array[$key];
    if (in_array($_POST['$search'], $val)) {
    #if ($val <> 'emiel') {
      echo $key ." = ". $val ." <br> ";
      }
    next($array);
    }

*/
?>
