% rebase('osnova.tpl', naslov='Id knjige')

<div>
<form action="/poisciKnjigo/">
Naslov knjige: <input type="text" name="naslov">
<button type="submit">Najdi!</button>
</form>
</div>

<table>
  <tr>
    <th>Naslov knjige</th>
    <th>ID knjige</th>
  </tr>
  % for knjiga in knjige:
  <tr>
    <td>{{knjiga['naslov']}}</td>
    <td>{{knjiga['id']}}</td>
  </tr>
  % end
</table>
</body>
</html>