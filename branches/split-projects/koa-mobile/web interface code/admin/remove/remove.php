<html> 
<head> 
<title>Remove entry from MySQL Database</title> 
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"> 
</head> 

<body> 

<form action="" method="post" enctype="multipart/form-data" name="removeform">
  <table border="1" cellspacing="1" style="border-collapse: collapse" bordercolor="#000066" width="95%" cellpadding="5">

	<tr>
	<td colspan="3" bgcolor="#B5CBEF" height="17" width="100%" bordercolor="#FFFFFF" background="tile_back.gif"> <p align="left\><b><font face="Verdana" size="2" color="#FFFFFF"><img border="0" src="nav_m.gif" width="8" height="8">
		<font face='Verdana' size=2 color='#FFFFFF'><b> Remove an entry &nbsp; </font><font face="Verdana" size="2" color="#000066"> </font></b>
	</td>
	</tr>
<tr>
	<td colspan="3" bgcolor="#B5CBEF" height="16" width="100%" bordercolor="#FFFFFF" background="tile_sub.gif">
	<font face="Verdana" size="2" color="#000066"><input name="idnum" type="text"> <input name="remove" type="submit" id="remove" value=" Remove "> </td>
	&nbsp;</font>
</tr>
	
	<tr>
		
 	  		<td height="30" width="20" bgcolor="#EFF3F7" bordercolor="#FFFFFF"><font color="blue"><strong>ID</strong></td>
			<td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF"><font color="blue"><strong>Topic</strong></td>	
	</tr>


	<?php

	mysql_connect('csserver.ucd.ie','s01bf213','eamonnlawler');
	mysql_select_db(voting) or die('Incorrect username or password!'); 
	$result = mysql_query("SELECT idNum, topic FROM topic");
	while($row = mysql_fetch_array($result))
	{
		$id = $row["idNum"];
		$topicstring = $row["topic"];
	?>
		<tr>
 	  		<td height="30" width="20" bgcolor="#EFF3F7" bordercolor="#FFFFFF"><?php echo $id ?></td>
			<td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF"><?php echo $topicstring ?></td>	
		</tr>
		
	<?php
	}
	mysql_free_result($result);
	mysql_close();
	?>
	
	<br>

  </table> 
</form> 


<?php
 
if(isset($_POST['remove'])) 
{
  mysql_connect('csserver.ucd.ie','s01bf213','eamonnlawler');
  mysql_select_db(voting) or die('Incorrect username or password!'); 
  
  
  $id = $_POST['idnum'];

  // Update fields in topic accordingly
  mysql_query("DELETE FROM topic WHERE idNum=$id");

  mysql_query("DELETE FROM topicAnswers WHERE topicId=$id");

  
  mysql_close();

?>

      <script type="text/javascript">
	alert("Topic removed successfully!");
	window.location.href = "http://csserver.ucd.ie/~s02bf067/web/inline.htm";

	</script>

<?php
}
?>

</body>
</html>