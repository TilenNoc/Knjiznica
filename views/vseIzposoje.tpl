% rebase('osnova.tpl', naslov='Izposoje', motivacija='motivacija.png')
<div class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px">

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

</div>
</body>
</html>