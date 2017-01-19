% rebase('osnova.tpl', naslov='Id osebe', motivacija='motivacija.png')

<form action="/poisciOsebo/">
Ime osebe: <input type="text" name="ime">
Priimek osebe: <input type="text" name="priimek">
<button type="submit">Najdi</button>
</form>

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
