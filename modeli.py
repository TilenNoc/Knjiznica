import sqlite3
from datetime import date, datetime, timedelta

con = sqlite3.connect('Knjiznica.db')

def osebaIzposojen(ime =''):
    '''Funkcija bo vrnila seznam oseb, ki imajo izposojene knjige in stevilo izposojenih knjig'''
    if len(ime)==0:
        for el in con.execute('''select distinct st_izkaznice,ime,priimek,count(st_izkaznice)
    from izposoja join oseba on (id_osebe=st_izkaznice) group by st_izkaznice'''):
                          print(el)
    else:
        for el in con.execute('''select distinct st_izkaznice,ime,priimek,count(st_izkaznice)
    from izposoja join oseba on (id_osebe=st_izkaznice) group by st_izkaznice'''):
            if ime == (el[1]+' '+el[2]):
                return(el)

def osebaIzposojenTrenutno(ime =''):
    '''Funkcija bo vrnila seznam oseb, ki imajo izposojene knjige in stevilo izposojenih knjig'''
    if len(ime)==0:
        for el in con.execute('''select distinct st_izkaznice,ime,priimek,count(st_izkaznice)
    from izposoja join oseba on (id_osebe=st_izkaznice) where datum_vracila is null group by st_izkaznice;'''):
                          print(el)
    else:
        for el in con.execute('''select distinct st_izkaznice,ime,priimek,count(st_izkaznice)
    from izposoja join oseba on (id_osebe=st_izkaznice) where datum_vracila is null group by st_izkaznice;'''):
            if ime == (el[1]+' '+el[2]):
                return(el)

def knjigaProsta(naslov):
    '''Funkcija bo preverila če je knjiga na zalogi'''
    steviloVseh = con.execute('select stevilo from knjige where naslov = ?',[naslov]) #koliko teh kjig imamo
    try:
        st = steviloVseh.fetchone()[0]
    except:
        raise Exception('Napačn naslov oziroma ni knjige')
    if st == None:
        return 0
    return st

def zamudnina():
    '''izračuna zamudnino za posamezno izposojo'''
    cena = 0.05
    sql = '''SELECT id_osebe AS oseba,
       potek_izposoje,
       datum_vracila
  FROM izposoja
 WHERE datum_vracila > potek_izposoje OR 
       datum_vracila IS NULL; 
        '''
    for el in con.execute(sql):
        oseba, rok, vracilo = el[0], el[1], el[2]
        if vracilo is None:
            vracilo = datetime.now().date()
            v = vracilo
        else:
            vracilo = vracilo.split('-')
            v = date(int(vracilo[0]),int(vracilo[1]),int(vracilo[2]))
        rok = rok.split('-')
        r = date(int(rok[0]),int(rok[1]),int(rok[2]))
        razlika = v-r
        razlika = razlika.days
        znesek = round(cena * razlika,2)
        print(oseba,razlika, znesek)

def izposoja(idOsebe, idKnjige):
    '''naredimo izposojo'''
    datumIzposoje = datetime.now().date()
    datumVracila = datumIzposoje + timedelta(days = 14)
    sql = '''INSERT INTO izposoja (id_osebe, id_knjige, datum_izposoje, potek_izposoje) VALUES (?,?,?,?)'''
    con.execute(sql,[idOsebe, idKnjige, datumIzposoje, datumVracila])
    con.commit()

def vpisOsebe(ime, priimek, datumRojstva, mail, clanarina, zamudnina = 0):
    '''v bazo dodamo novega člana'''
    sql = '''INSERT INTO oseba (ime, priimek, datum_rojstva, mail, clanarina, zamudnina) VALUES (?,?,?,?,?,?)'''
    con.execute(sql,[ime, priimek, datumRojstva, mail, clanarina, zamudnina])
    con.commit()

def vpisKnjige(naslov, avtor, zalozba, leto_izdaje, ponatis, stevilo):
    '''v bazo dodamo novo knjigo'''
    sql = '''INSERT INTO knjige (naslov, avtor, zalozba, leto_izdaje, ponatis, stevilo) VALUES (?,?,?,?,?,?)'''
    con.execute(sql,[naslov, avtor, zalozba, leto_izdaje, ponatis, stevilo])
    con.commit()

def vraciloKnjige(idOsebe, idKnjige):
    '''Oseba naredi vracilo knjige'''
    datumVracila = datetime.now().date()
    sql = '''update izposoja set datum_vracila =? where id_osebe=? and id_knjige=?'''
    con.execute(sql,[datumVracila,idOsebe,idKnjige])
    con.commit()

def rezervacijaKnjige(idOsebe, idKnjige):
    '''Oseba naredi rezarvacijo knjige'''
    datumRezervacije = datetime.now().date()
    sql = '''INSERT INTO rezervacija (id_osebe, id_knjige, kdaj) VALUES (?,?,?)'''
    con.execute(sql,[idOsebe, idKnjige, datumRezervacije])
    con.commit()
