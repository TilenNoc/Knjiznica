<!DOCTYPE html>
<html>
<head>
<style>
body {border-radius: 16px;}

motivacija {
	float:right;
}

.naslov {
	margin-left:40%;
	text-align:center;
	font-family:'Raleway',sans-serif;
	width: 500px;	font size="100"
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
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover {
    background-color: #66ccff;
}
li ul
     { 
         display:none; 
         position:absolute;
		 left: 150px;
		 top:45px;
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
<div class = "naslov">
<h1 style = "float:left; width:auto;font size="100""> KNJIŽNICA </h1>
<img id = "motivacija" width = "100" height = "100" src = "views/{{motivacija}}"/>
</div>

<div style = "clear:both">
<hr size = "40"/>
<ul class = "zaviti-robovi">
 <img src="views/{{knjiznicar}}" width = "500" height = 348 align="middle"><div style="text-align: center;"> <li><a href="#">Knjige</a>
	<ul class = "zaviti-robovi">
		<li><a href = "/vpisKnjige/">Vnesi novo knjigo</a></li>
		<li><a href = "/knjigaProsta/">Zaloga knjig</a></li>
	</ul>
  </li>
  <li><a href="/izposoja/">Izposoja Knjige</a></li>
  <li><a href="/osebaIzposojenTrenutno/">Seznam izposojenih knjig</a></li> <li><a href="/zamudnina/">Zamudnine</a></li> 
<li><a href="/vraciloKnjige/">Vračilo knjige</a></li> <li><a href="/rezervacijaKnjige/">Rezervacija knjige</a></li>  
<ul class = "zaviti-robovi">
  <li><a href="#">Osebe</a>
	<ul class = "zaviti-robovi">
		<li><a href = "/vpisOsebe/">Vnesi novo osebo</a></li>
		<li><a href = "/zamudnina/">Zamudnina neke osebe</a></li>
	</ul>
  </li>
</ul>
</div>
</body>
</html>