% rebase('osnova.tpl', naslov='Rezervacija', motivacija='motivacija.png')
<div id=c class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px; width: 300px">
<form method="post" action="/rezervacijaKnjige/">
ID osebe: <input type="text" name="idOsebe">
ID knjige: <input type="text" name="idKnjige">
<button type="submit">Rezerviraj!</button>
</form>
</div>
</body>
</html>