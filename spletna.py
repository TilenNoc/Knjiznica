from bottle import route, run, template,static_file, get, post, request, redirect
import modeli


@route('/')
def domaca_stran():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('domaca_stran', knjiznicar = slika_ime1, motivacija = slika_ime2)

@get('/knjigaProsta/')
def knjigaProsta():
    idKnjige = request.query.idKnjige
    if idKnjige:
        return template('knjigaProsta', idKnjige = idKnjige, knjigaProsta = modeli.knjigaProsta(idKnjige))
    else:
        return template('knjigaProsta', idKnjige = idKnjige, knjigaProsta = None)

@get('/osebaIzposojenTrenutno/')
def osebaIzposojenTrenutno():
    idOsebe = request.query.idOsebe
    if idOsebe:
        return template('osebaIzposojenTrenutno', idOsebe = idOsebe, osebaIzposojenTrenutno = modeli.osebaIzposojenTrenutnoEdn(idOsebe))
    else:
        return template('osebaIzposojenTrenutno', osebaIzposojenTrenutno = None)

@get('/vseIzposoje/')
def vseIzposoje():
    return template('vseIzposoje', vseIzposoje = modeli.osebaIzposojenTrenutno())

@get('/zamudnina/')
def zamudnina():
    idOsebe = request.query.idOsebe
    if idOsebe:
        return template('zamudnina', idOsebe = idOsebe, zamudnina = modeli.zamudninaOseba(idOsebe))
    else:
        return template('zamudnina', zamudnina = None)

@get('/poisciKnjigo/')
def poisciKnjigo():
    naslov = request.query.naslov
    knjige = modeli.poisciKnjigo(naslov)
    return template('poisciKnjigo', knjige=knjige)
   
@get('/poisciOsebo/')
def poisciOsebo():
    ime = request.query.ime
    priimek = request.query.priimek
    osebe = modeli.poisciOsebo(ime, priimek)
    return template('poisciOsebo', osebe=osebe)
   
@get('/zamudninaVsi/')
def zamudninaVsi():
    return template('zamudninaVsi', zamudnina = modeli.zamudnina())

@get('/izposoja/')
def izposoja():
    return template('izposoja')

@post('/izposoja/')
def izposoja():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.izposoja(idOsebe, idKnjige)
    redirect('/')

@get('/vpisKnjige/')
def vpisKnjige():
    return template('vpisKnjige')

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
    return template('vraciloKnjige')

@post('/vraciloKnjige/')
def vraciloKnjige():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.vraciloKnjige(idOsebe, idKnjige)
    redirect('/')

@get('/rezervacijaKnjige/')
def rezervacijaKnjige():
    return template('rezervacijaKnjige')

@post('/rezervacijaKnjige/')
def rezervacijaKnjige():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.rezervacijaKnjige(idOsebe, idKnjige)
    redirect('/')

@get('/opravljenaRezervacija/')
def opravljenaRezervacija():
    return template('opravljenaRezervacija')

@post('/opravljenaRezervacija/')
def opravljenaRezervacija():
    idOsebe = request.forms.get('idOsebe')
    idKnjige = request.forms.get('idKnjige')
    modeli.opravljenaRezervacija(idOsebe, idKnjige)
    redirect('/')
    
@get('/vpisOsebe/')
def vpisOsebe():
    return template('vpisOsebe')

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

