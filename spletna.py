from bottle import route, run, template,static_file, get, post, request
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
    return template('zamudnina', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/izposoja/')
def izposoja():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
##    idOsebe=int(request.query.idOsebe)
##    idKnjige=int(request.query.idKnjige)
    return template('izposoja', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/vpisKnjige/')
def vpisKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('vpisKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/knjigaProsta/')
def knjigaProsta():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('knjigaProsta', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/storitve/')
def osebaIzposojenTrenutno():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('osebaIzposojenTrenutno', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/osebaIzposojenTrenutno/')
def osebaIzposojenTrenutno():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('osebaIzposojenTrenutno', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/vraciloKnjige/')
def vraciloKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('vraciloKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/rezervacijaKnjige/')
def rezervacijaKnjige():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('rezervacijaKnjige', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/vpisOsebe/')
def vpisOsebe():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('vpisOsebe', knjiznicar = slika_ime1, motivacija = slika_ime2)

@route('/views/<motivacija>')
def serve_pictures(motivacija):
    return static_file(motivacija, root='views')



run(debug = True)
