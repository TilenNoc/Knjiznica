% rebase('osnova.tpl', naslov='Izposoje', motivacija='motivacija.png')
<div>

<form action="/osebaIzposojenTrenutno/">
ID osebe: <input type="text" name="idOsebe">
<button type="submit">Pokaži!</button>
</form>
<table>
  <tr>
    <th>ID osebe</th>
    <th>Ime</th>
	<th>Priimek</th>
	<th>Število izposojenih knjig</th>
  </tr>
  % if osebaIzposojenTrenutno != None:
		<tr>
			<td>{{osebaIzposojenTrenutno[0]}}</td>
			<td>{{osebaIzposojenTrenutno[1]}}</td>
			<td>{{osebaIzposojenTrenutno[2]}}</td>
			<td>{{osebaIzposojenTrenutno[3]}}</td>
		</tr>
  % end
</table>
</div>
</body>
</html>