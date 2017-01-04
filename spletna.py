from bottle import route, run, template,static_file, get, post, request, redirect
import modeli


@route('/')
def domaca_stran():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('domaca_stran', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/zamudnina/')
def zamudnina():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    idOsebe = request.query.idOsebe
    return template('zamudnina', knjiznicar = slika_ime1, motivacija = slika_ime2, idOsebe = idOsebe, zamudnina = modeli.zamudnina(idOsebe))

##@get('/zamudnina/<idOsebe>/')
##def poglej_zamudnino(idOseba):
##    return template('zamudnina',zamudnina = modeli.zamudnina(idOsebe))

@route('/izposoja/')
def izposoja():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    idOsebe = request.query.idOsebe
    idKnjige = request.query.idKnjige
    return template('izposoja', knjiznicar = slika_ime1, motivacija = slika_ime2, idOsebe = idOsebe, idKnjige = idKnjige, izposoja = modeli.izposoja(idOsebe, idKnjige))

##@get('/izposoja/')
##def izposoja():
##    slika_ime1 = 'knjiznicar.png'
##    slika_ime2 = 'motivacija.png'
##    return template('izposoja', knjiznicar = slika_ime1, motivacija = slika_ime2)
##
##@post('/izposoja/')
##def izposoja():
##    idOsebe = request.forms.get('idOsebe')
##    idKnjige = request.forms.get('idKnjige')
##    modeli.izposoja(idOsebe, idKnjige)
##    redirect('/')

@route('/vpisKnjige/')
def vpisKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    naslov = request.query.naslov
    avtor = request.query.avtor
    zalozba = request.query.zalozba
    leto_izdaje = request.query.leto_izdaje
    ponatis = request.query.ponatis
    stevilo = request.query.stevilo
    return template('vpisKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2, naslov=naslov, avtor=avtor, zalozba=zalozba, leto_izdaje=leto_izdaje, ponatis=ponatis, stevilo=stevilo, vpisKnjige = modeli.vpisKnjige(naslov, avtor, zalozba, leto_izdaje, ponatis, stevilo))

@route('/knjigaProsta/')
def knjigaProsta():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    naslov = request.query.naslov
    return template('knjigaProsta', knjiznicar = slika_ime1, motivacija = slika_ime2, naslov = naslov, knjigaProsta = modeli.knjigaProsta(naslov))

@route('/storitve/')
def osebaIzposojenTrenutno():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    ime = request.query.ime
    return template('osebaIzposojenTrenutno', knjiznicar = slika_ime1, motivacija = slika_ime2, ime = ime, osebaIzposojenTrenutno = modeli.osebaIzposojenTrenutno(ime))

@route('/vraciloKnjige/')
def vraciloKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    idOsebe = request.query.idOsebe
    idKnjige = request.query.idKnjige
    return template('vraciloKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2, idOsebe = idOsebe, idKnjige = idKnjige, vraciloKnjige = modeli.vraciloKnjige(idOsebe, idKnjige))

@route('/rezervacijaKnjige/')
def rezervacijaKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    idOsebe = request.query.idOsebe
    idKnjige = request.query.idKnjige
    return template('rezervacijaKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2, idOsebe = idOsebe, idKnjige = idKnjige, rezervacijaKnjige = modeli.rezervacijaKnjige(idOsebe, idKnjige))
    
@route('/vpisOsebe/')
def vpisOsebe():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    ime = request.query.ime
    priimek = request.query.priimek
    datumRojstva = request.query.datumRojstva
    mail = request.query.mail
    clanarina = request.query.clanarina
    return template('vpisOsebe', knjiznicar = slika_ime1, motivacija = slika_ime2, ime=ime, priimek=priimek, datumRojstva=datumRojstva, mail=mail, clanarina=clanarina, vpisOsebe = modeli.vpisOsebe(ime, priimek, datumRojstva, mail, clanarina, zamudnina = 0))

@route('/views/<motivacija>')
def serve_pictures(motivacija):
    return static_file(motivacija, root='views')



run(debug = True)

