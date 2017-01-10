% rebase('osnova.tpl', naslov='Izposoja knjige', motivacija='motivacija.png')

<div id=c class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px; width">
<form method="post" action="/izposoja/">
ID osebe: <input type="text" name="idOsebe">
ID knjige: <input type="text" name="idKnjige">
<button type="submit">Izposodi!</button>
</form>
</div>

</body>
</html>
