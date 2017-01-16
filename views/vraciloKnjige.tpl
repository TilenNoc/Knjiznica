% rebase('osnova.tpl', naslov='Vračilo knjige', motivacija='motivacija.png')
<div id=c class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px; width: 300px">
<form method="post" action="/vraciloKnjige/">
ID izkaznice osebe: <input type="text" name="idOsebe">
ID vrnjene knjige: <input type="text" name="idKnjige">
<button type="submit">Vrni!</button>
</form>
</div>
</body>
</html>