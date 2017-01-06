% rebase('osnova.tpl', naslov='Izposoja knjige', motivacija='motivacija.png')
<div>
<form method="post" action="/izposoja/">
ID osebe: <input type="text" name="idOsebe">
ID knjige: <input type="text" name="idKnjige">
<button type="submit">Izposodi!</button>
</form>
</div>
</body>
</html>