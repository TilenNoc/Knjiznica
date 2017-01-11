<!DOCTYPE html>
<html>
<head>
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	
<style>
#parent{
display:flex;
flex-flow: column;
}
#a{order:1;}
#b{order:2;}
#c{order:3;}
#d{order:4;}
body {background: url(/views/knjiznicar.png) no-repeat 350px 250px;}

table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
tr:nth-child(odd) {
	background-color: #ffffff;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
motivacija {
	float:right;
}
.naslov {
	margin-left:37%;
	text-align:center;
	font-family:'Raleway',sans-serif;
	width: 500px;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    background-color: #3399ff;
    max-width: 150px;
	position:relative;
}
li {
  position: relative
}
li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
	font-family:'Raleway',sans-serif;
    text-decoration: none;
}
li a:hover {
    background-color: #66ccff;
}
li ul
     { 
         display:none; 
		 position: absolute;
		 left: 150px;
		 top: 0px;
     }
li:hover ul{
	display:block;}
hr {background-color: #3399ff;
	margin: 0; 
	border-radius:10px;
	}
	
</style>
</head>

<body>
<div id="parent">
<div id=a class = "naslov">
<h1 style = "float:left; width:auto;font-size:50px;"> {{naslov}} </h1>
<img id = "motivacija" width = "150" height = "150" src = "/views/{{motivacija}}"/>
</div>
<div >
</div>
<div id= b style = "clear:both">
<hr size = "40"/>
<ul class = "tabele">
 <div style="text-align: center;">
	<li><a href="/"><b>Domov</b></a></li> 
	<li><a href="/izposoja/">Izposoja Knjige</a></li> 
	<li><a href="#">Knjige</a>
	<ul class = "tabele">
		<li><a href = "/vpisKnjige/">Vnesi novo knjigo</a></li>
		<li><a href = "/knjigaProsta/">Zaloga knjig</a></li>
	</ul>
	</li>
	<li><a href="#">Osebe</a>
	<ul class = "tabele2">
		<li><a href = "/vpisOsebe/">Vnesi novo osebo</a></li>
		<li><a href = "/zamudnina/">Zamudnina neke osebe</a></li>
		<li><a href="/osebaIzposojenTrenutno/">Seznam izposojenih knjig osebe</a></li>
	</ul>
	</li>
	<li><a href="/vseIzposoje/">Seznam izposojenih knjig</a></li>
	<li><a href="/zamudninaVsi/">Zamudnine vseh</a></li> 
	<li><a href="/vraciloKnjige/">Vračilo knjige</a></li> 
	<li><a href="/rezervacijaKnjige/">Rezervacija knjige</a></li> 
	<li><a href="/opravljenaRezervacija/">Zaključi rezervacijo</a></li>
	<li><a href="/poisciKnjigo/">Poišči ID knjige</a></li> 
	<li><a href="/poisciOsebo/">Poišči ID osebe</a></li> 
</div>
</div>

{{!base}}
</body>
</html>
