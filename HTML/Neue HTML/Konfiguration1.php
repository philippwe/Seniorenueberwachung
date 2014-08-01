<!DOCTYPE html>
<html>
	<head>
	 <title>Raspberry Pi - Konfiguration</title>
<link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.css" />
<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<script src="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.js"></script>
	</head>
		<body>
		<?php
		include ("insert.php");
		
		?>




		 <div data-role = 'header'>
		   <h1> Konfiguration</h1>
		 </div>

		 <div data-role = 'content'>
			<form action="schreiben_konfiguration.php" method="GET">

 			<label>Name des zu Überwachenden</label>
			 <input type="text" name="Name" value="<?php echo $curr_konf[0] ?>"/>

 			<label>Zeitintervall</label>
			 <input type="text" name="Zeit" value="<?php echo $curr_konf[1] ?>" />
			
			 <label for="EMAILS">E-Mail Adressen</label>
       			 <textarea id="EMAILS" name="EMAILS" cols="35"><?php for($i=2; $i < count($curr_konf); $i++)
   {
   echo $curr_konf[$i]; } ?> </textarea>
			
			<div data-role ='navbar'>
			<ul>
				<input name="EMAILS" value="Eintragen" type="submit">
			</ul>
			</div>
		</form>
		 </div>
		 
		 <div data-role = 'footer'>
		 </div>
		 
		</body>
</html>
