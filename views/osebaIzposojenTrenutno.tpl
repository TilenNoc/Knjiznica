% rebase('osnova.tpl', naslov='Izposoje', motivacija='motivacija.png')
<div>

<form action="/osebaIzposojenTrenutno/">
Ime in priimek osebe: <input type="text" name="ime">
<button type="submit">Pokaži!</button>
</form>

<% for el in osebaIzposojenTrenutno:
	id, ime, priimek, stKnjig = el
	izpis = ('ID osebe: ' + str(id) + ', Ime: ' + ime + ', Priimek: ' + priimek + ', Število izposojenih knjig: ' + str(stKnjig))
%>
{{izpis}}<br>

</div>
</body>
</html>