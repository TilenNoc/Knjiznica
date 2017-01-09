% rebase('osnova.tpl', naslov='Id osebe')

<div>
<form action="/poisciOsebo/">
Ime osebe: <input type="text" name="ime">
Priimek osebe: <input type="text" name="priimek">
<button type="submit">Najdi</button>
</form>
</div>

<table>
  <tr>
    <th>Ime</th>
    <th>Primek</th>
    <th>Id Izkaznice</th>
  </tr>
  % for oseba in osebe:
  <tr>
    <td>{{oseba['ime']}}</td>
    <td>{{oseba['priimek']}}</td>
    <td>{{oseba['st_izkaznice']}}</td>
  </tr>
  % end
</table>

</body>
</html>