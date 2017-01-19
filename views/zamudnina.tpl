% rebase('osnova.tpl', naslov='Zamudnine', motivacija='motivacija.png')

<form action="/zamudnina/">
ID osebe: <input type="text" name="idOsebe">
<button type="submit">Pokaži!</button>
</form>

<table>
  <tr>
    <th>ID osebe</th>
    <th>ID knjige</th>
	<th>Zamujeni dnevi</th>
	<th>Zamudnina</th>
  </tr>
  % if zamudnina is not None:
		% if(zamudnina !="Ni zamudnine"):
			<tr>
				<td>{{zamudnina[0]}}</td>
				<td>{{zamudnina[1]}}</td>
				<td>{{zamudnina[2]}}</td>
				<td>{{zamudnina[3]}}</td>
			</tr>
		% else:
			{{zamudnina}}
		% end
% end
</table>
