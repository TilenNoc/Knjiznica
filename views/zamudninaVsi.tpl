% rebase('osnova.tpl', naslov='Zamudnine Vsi', motivacija='motivacija.png')
<div>

<form action="/zamudninaVsi/">

</form>

<% for el in zamudnina:
	oseba, knjiga, razlika, placilo = el
	izpis = ('Oseba: ' + str(oseba) + ', Knjiga: ' + str(knjiga) + ', Zamujeni dnevi: ' + str(razlika) + ', Zamudnina: ' + str(placilo))
%>
{{izpis}}<br>

</div>
</body>
</html>