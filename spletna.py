from bottle import route, run, template
import modeli

@route('/')
def index():
    return template('glavna')

@route('/pomoc/')
def pomoc():
    return 'Pojdi na stran /delitelji/xxx/ za delitelje števila xxx.'

##@route('/delitelji/<n>/')
##def delitelji(n):
##    n = int(n)
##    return template('seznam_deliteljev', n=n, delitelji=modeli.delitelji(n))

run(debug=True)
