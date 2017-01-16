% rebase('osnova.tpl', naslov='Zamudnine Vsi', motivacija='motivacija.png')

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
