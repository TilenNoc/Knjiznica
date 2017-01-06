% rebase('osnova.tpl', naslov='Id osebe', motivacija='motivacija.png')
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>

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
  <tr>
    <td>name</td>
    <td>name="priimek"</td>
    <td>{{poisciOsebo}}</td>
  </tr>
</table>

</body>
</html>