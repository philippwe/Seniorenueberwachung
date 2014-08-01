<?php
$f = fopen("Konfiguration.txt", "r");
$curr_konf = array();

while (!feof($f)){

	array_push($curr_konf, fgets($f));

}

fclose($f);
?>
