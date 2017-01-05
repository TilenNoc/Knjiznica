% rebase('osnova.tpl', naslov='Vpis osebe', motivacija='motivacija.png')
<div>
<form method="post" action="/vpisOsebe/">
Ime: <input type="text" name="ime">
Priimek: <input type="text" name="priimek">
Datum rojstva: <input type="text" name="datumRojstva">
Mail: <input type="text" name="mail">
Članarina: <input type="text" name="clanarina">
<button type="submit">Dodaj!</button>
</form>
</div>
</body>
</html>