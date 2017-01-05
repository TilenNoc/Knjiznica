% rebase('osnova.tpl', naslov='Zamudnine', motivacija='motivacija.png')
<div>

<form action="/zamudnina/">
ID osebe: <input type="text" name="idOsebe">
<button type="submit">Pokaži!</button>
</form>

<% if zamudnina is not None:
	oseba, knjiga, razlika, placilo = zamudnina
	izpis = ('Oseba: ' + str(oseba) + ', Knjiga: ' + str(knjiga) + ', Zamujeni dnevi: ' + str(razlika) + ', Zamudnina: ' + str(placilo))
%>
{{izpis}}<br>

</div>
</body>
</html>