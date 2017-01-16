% rebase('osnova.tpl', naslov='Zamudnine Vsi', motivacija='motivacija.png')
<div id=c class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px; width: 300px">

<form action="/zamudninaVsi/">

</form>
<table>
  <tr>
    <th>ID osebe</th>
    <th>ID knjige</th>
	<th>Zamujeni dnevi</th>
	<th>Zamudnina</th>
  </tr>
  % for el in zamudnina:
		<tr>
			<td>{{el[0]}}</td>
			<td>{{el[1]}}</td>
			<td>{{el[2]}}</td>
			<td>{{el[3]}}</td>
		</tr>
  % end
</table>


</div>
</body>
</html>