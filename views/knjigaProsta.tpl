% rebase('osnova.tpl', naslov='Zaloga knjig', motivacija='motivacija.png')

<div id=c class = "izpis" style = "float-left; position: absolute; left: 150px; top: 158px; width: 300px">

<form action="/knjigaProsta/">
ID knjige: <input type="text" name="idKnjige">
<button type="submit">Poglej!</button>
</form>

<table>
  <tr>
    <th>ID knjige</th>
    <th>Na zalogi</th>
  </tr>
	<tr>
	%if knjigaProsta!=None:
		<td>{{knjigaProsta[0]}}</td>
		<td>{{knjigaProsta[1]}}</td>
	%end
	</tr>
% end
</table>
</div>
</body>
</html>