% rebase('osnova.tpl', naslov='Rezervacija', motivacija='motivacija.png')

<form method="post" action="/rezervacijaKnjige/">
ID osebe: <input type="text" name="idOsebe">
ID knjige: <input type="text" name="idKnjige">
<button type="submit">Rezerviraj!</button>
</form>
