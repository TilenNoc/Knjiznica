% rebase('osnova.tpl', naslov='Izposoja knjige', motivacija='motivacija.png')
<div>
<form method="post" action="/izposoja/">
<li>ID osebe: <input type="text" name="idOsebe"></li>
<li>ID knjige: <input type="text" name="idKnjige"></li>
<button type="submit">Izposodi!</button>
</form>
</div>
</body>
</html>