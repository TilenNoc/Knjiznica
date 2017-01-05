% rebase('osnova.tpl', naslov='Vračilo knjige', motivacija='motivacija.png')
<div>
<form action="/vraciloKnjige/">
ID izkaznice osebe: <input type="text" name="idOsebe">
ID vrnjene knjige: <input type="text" name="idKnjige">
<button type="submit">Vrni!</button>
</form>
</div>
</body>
</html>