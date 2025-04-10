<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
<?php 
 $file = fopen('listelivre.txt','a');
 $livres = $_POST['code'] . ":" . $_POST['titre'] . ':' . $_POST['categorie'] . ':' . $_POST['PV'] .':'.$_POST['QV'];
 fwrite($file, $livres);
 echo '<h1> Livres ajouté avec succes !</h1>';
 fclose($file);
 ;
  ?>
  
  