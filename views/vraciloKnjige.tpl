% rebase('osnova.tpl', naslov='Vračilo knjige', motivacija='motivacija.png')

<form method="post" action="/vraciloKnjige/">
ID izkaznice osebe: <input type="text" name="idOsebe">
ID vrnjene knjige: <input type="text" name="idKnjige">
<button type="submit">Vrni!</button>
</form>
