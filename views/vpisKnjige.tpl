% rebase('osnova.tpl', naslov='Nove knjige', motivacija='motivacija.png')
<div id=c class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px; width: 300px">
<form method="post" action="/vpisKnjige/">
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