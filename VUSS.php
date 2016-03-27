<?php
$search = $_POST['search'];
$text = file_get_contents("output.txt", "w+");
$lines = ($text . "\r\n");
$str = strstr($text, $_POST['search']);
if ($str == false){
  echo "Sorry! The email address for '$search' does not exists in this database.";
} else {
  echo "Our database does contain an email address of '$search'.\n<br />Please scroll through the email addresses below :)\n<br />\n<br />";
}
if ($str !== false){
  echo ("hein.van.den.berg2@gmail.com\n<br />
  contactsupport@readspeaker.com\n<br />
  m.lamers@vu.nl\n<br />
  emiel.van.miltenburg@vu.nl\n<br />
  lora.aroyo@vu.nl\n<br />
  z.huang@vu.nl\n<br />
  frank.van.harmelen@cs.vu.nl\n<br />
  guus.schreiber@vu.nl\n<br />
  hoekstra@uva.nl\n<br />
  wouter@vanatteveldt.com\n<br />
  a.m.baars@vu.nl\n<br />
  e.j.miedzobrodzka@vu.nl\n<br />
  b.beersma@vu.nl\n<br />
  j.p.kalkman@vu.nl\n<br />
  f.ten.holder@vu.nl\n<br />
  sg.sileno@uva.nl\n<br />
  a.w.f.boer@uva.nl");
}

/* THINGS TRIED
$search = $_POST['search'];
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
