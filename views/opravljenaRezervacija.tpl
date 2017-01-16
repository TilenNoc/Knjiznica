% rebase('osnova.tpl', naslov='Zaključek',  motivacija='motivacija.png')

<form method="post" action="/opravljenaRezervacija/">
ID osebe: <input type="text" name="idOsebe">
ID knjige: <input type="text" name="idKnjige">
<button type="submit">Zaključi!</button>
</form>
