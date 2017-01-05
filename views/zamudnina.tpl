% rebase('osnova.tpl', naslov='Zamudnine', motivacija='motivacija.png')
<div>

<form action="/zamudnina/">
ID osebe: <input type="text" name="idOsebe">
<button type="submit">Pokaži!</button>
</form>
{{zamudnina}}
</div>
</body>
</html>