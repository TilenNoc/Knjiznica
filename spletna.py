from bottle import route, run, template,static_file, get, post, request, redirect
import modeli


@route('/')
def domaca_stran():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('domaca_stran', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/knjigaProsta/')
def knjigaProsta():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    naslov = request.query.naslov
    return template('knjigaProsta', knjiznicar = slika_ime1, motivacija = slika_ime2, naslov = naslov, knjigaProsta = modeli.knjigaProsta(naslov))

@route('/osebaIzposojenTrenutno/')
def osebaIzposojenTrenutno():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    ime = request.query.ime
    return template('osebaIzposojenTrenutno', knjiznicar = slika_ime1, motivacija = slika_ime2, ime = ime, osebaIzposojenTrenutno = modeli.osebaIzposojenTrenutno(ime))

##@route('/zamudnina/')
##def zamudnina():
##    slika_ime1 = 'knjiznicar.png'
##    slika_ime2 = 'motivacija.png'
##    idOsebe = request.query.idOsebe
##    return template('zamudnina', knjiznicar = slika_ime1, motivacija = slika_ime2, idOsebe = idOsebe, zamudnina = modeli.zamudnina(idOsebe))

@get('/zamudnina/')
def zamudnina():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    idOsebe = request.query.idOsebe
    if idOsebe:
        return template('zamudnina',knjiznicar = slika_ime1, motivacija = slika_ime2, idOsebe = idOsebe, zamudnina = modeli.zamudninaOseba(idOsebe))
    else:
        return template('zamudnina',knjiznicar = slika_ime1, motivacija = slika_ime2, zamudnina = modeli.zamudnina())

@post('/zamudnina/')
def zamudnina():
    
   
@get('/izposoja/')
def izposoja():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('izposoja', knjiznicar = slika_ime1, motivacija = slika_ime2)

@post('/izposoja/')
def izposoja():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.izposoja(idOsebe, idKnjige)
    redirect('/')

@get('/vpisKnjige/')
def vpisKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('vpisKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2)

@post('/vpisKnjige/')
def vpisKnjige():
    naslov = request.forms.get('naslov')
    avtor = request.forms.get('avtor')
    zalozba = request.forms.get('zalozba')
    leto_izdaje = request.forms.get('leto_izdaje')
    ponatis = request.forms.get('ponatis')
    stevilo = request.forms.get('stevilo')
    modeli.vpisKnjige(naslov, avtor, zalozba, leto_izdaje, ponatis, stevilo)
    redirect('/')   

@get('/vraciloKnjige/')
def vraciloKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('vraciloKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2)

@post('/vraciloKnjige/')
def vraciloKnjige():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.vraciloKnjige(idOsebe, idKnjige)
    redirect('/')

@get('/rezervacijaKnjige/')
def rezervacijaKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('rezervacijaKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2)

@post('/rezervacijaKnjige/')
def rezervacijaKnjige():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.rezervacijaKnjige(idOsebe, idKnjige)
    redirect('/')
    
@get('/vpisOsebe/')
def vpisOsebe():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('vpisOsebe', knjiznicar = slika_ime1, motivacija = slika_ime2)

@post('/vpisOsebe/')
def vpisOsebe():
    ime = request.forms.get('ime')
    priimek = request.forms.get('priimek')
    datumRojstva = request.forms.get('datumRojstva')
    mail = request.forms.get('mail')
    clanarina = request.forms.get('clanarina')
    modeli.vpisOsebe(ime, priimek, datumRojstva, mail, clanarina, zamudnina = 0)
    redirect('/')

@route('/views/<motivacija>')
def serve_pictures(motivacija):
    return static_file(motivacija, root='views')



run(debug = True)

