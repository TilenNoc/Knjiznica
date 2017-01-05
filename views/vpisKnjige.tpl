% rebase('osnova.tpl', naslov='Nove knjige', motivacija='motivacija.png')
<div>
<form action="/vpisKnjige/">
Naslov: <input type="text" name="naslov">
Avtor: <input type="text" name="avtor">
Založba: <input type="text" name="zalozba">
Leto izdaje: <input type="text" name="leto_izdaje">
Ponatis: <input type="text" name="ponatis">
Število: <input type="text" name="stevilo">
<button type="submit">Dodaj!</button>
</form>
</div>
</body>
</html>