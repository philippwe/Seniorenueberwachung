<?php
$daten2 = $_GET['Zeit'];
$daten = $_GET['EMAILS'];
$daten_name = "Konfiguration.txt";
$fp = fopen($daten_name, "w");
fwrite($fp, $daten2);
fwrite($fp, "\r\n");
fwrite($fp, $daten);
fclose($fp);
?>
