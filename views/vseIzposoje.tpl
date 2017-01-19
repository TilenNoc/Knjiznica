% rebase('osnova.tpl', naslov='Izposoje', motivacija='motivacija.png')

<form action="/vseIzposoje/">

</form>

<table>
  <tr>
    <th>ID osebe</th>
    <th>Ime</th>
	<th>Priimek</th>
	<th>Število izposojenih knjig</th>
  </tr>
  % for el in vseIzposoje:
		<tr>
			<td>{{el[0]}}</td>
			<td>{{el[1]}}</td>
			<td>{{el[2]}}</td>
			<td>{{el[3]}}</td>
		</tr>
  % end
</table>
