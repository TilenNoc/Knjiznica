% rebase('osnova.tpl', naslov='Id knjige')

<form action="/poisciKnjigo/">
Naslov knjige: <input type="text" name="naslov">
<button type="submit">Najdi!</button>
</form>

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
