% rebase('osnova.tpl', naslov='Izposoje', motivacija='motivacija.png')
<div>

<form action="/osebaIzposojenTrenutno/">
ID osebe: <input type="text" name="idOsebe">
<button type="submit">Pokaži!</button>
</form>

% if osebaIzposojenTrenutno != None:
	% id, ime, priimek, stKnjig = osebaIzposojenTrenutno
	<h3>{{ime}}</h3>
% end

</div>
</body>
</html>