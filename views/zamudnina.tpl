% rebase('osnova.tpl', naslov='Zamudnine', motivacija='motivacija.png')
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
<div>

<form action="/zamudnina/">
ID osebe: <input type="text" name="idOsebe">
<button type="submit">Pokaži!</button>
</form>

<% if zamudnina is not None:
		if len(zamudnina)!=4:
			izpis = ('Ni zamudnine')
		else:
			oseba, knjiga, razlika, placilo = zamudnina
			izpis = ('Oseba: ' + str(oseba) + ', Knjiga: ' + str(knjiga) + ', Zamujeni dnevi: ' + str(razlika) + ', Zamudnina: ' + str(placilo))

%>

{{izpis}}<br>

</div>

<table>
  <tr>
    <th>Oseba</th>
    <th>Knjiga</th>
    <th>Dnevi prekoračeno</th>
    <th>Plačilo</th>
  </tr>
  <tr>
    <td>oseba</td>
    <td>knjiga</td>
    <td>razlika</td>
    <td>placilo</td>
  </tr>
</table>

</body>
</html>