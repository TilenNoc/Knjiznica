from bottle import route, run, template,static_file, get, post, request
import modeli


@route('/')
def domaca_stran():
    slika_ime1 = 'knjiznicar.png'
    slika_ime2 = 'motivacija.png'
    return template('domaca_stran', slika = slika_ime1, motivacija = slika_ime2)

@route('/zamudnina/')
def zamudnina():
    return template('zamudnina')

@route('/izposoja/')
def izposoja():
    return template('izposoja')

@route('/vpisKnjige/')
def vpisKnjige():
    return template('vpisKnjige')

@route('/knjigaProsta/')
def knjigaProsta():
    return template('knjigaProsta')

@route('/storitve/')
def osebaIzposojenTrenutno():
    return template('osebaIzposojenTrenutno')

@route('/vraciloKnjige/')
def vraciloKnjige():
    return template('vraciloKnjige')

@route('/rezervacijaKnjige/')
def rezervacijaKnjige():
    return template('rezervacijaKnjige')

@route('/vpisOsebe/')
def vpisOsebe():
    return template('vpisOsebe')

@route('views/<motivacija>')
def serve_pictures(motivacija):
    return static_file(motivacija, root='views')

run(debug = True)
