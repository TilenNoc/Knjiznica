% rebase('osnova.tpl', naslov='Id knjige', motivacija='motivacija.png')
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
<form action="/poisciKnjigo/">
Naslov knjige: <input type="text" name="naslov">
<button type="submit">Najdi!</button>
</form>
</div>

<table>
  <tr>
    <th>Naslov knjige</th>
    <th>Id Izkaznice</th>
  </tr>
  <tr>
    <td>naslov</td>
    <td>{{poisciKnjigo}}</td>
  </tr>

</table>
</body>
</html>