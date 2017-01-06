import sqlite3
from datetime import date, datetime, timedelta

con = sqlite3.connect('Knjiznica.db')

def osebaIzposojenEdn(idOsebe):
    '''Funkcija bo vrnila  izposojene knjige in stevilo izposojenih knjig od osebe'''
    sql = '''SELECT DISTINCT st_izkaznice, ime, priimek, COUNT(st_izkaznice)
    FROM izposoja
    JOIN oseba
    ON (id_osebe=st_izkaznice)
    GROUP BY st_izkaznice'''
    for el in con.execute(sql):
        if idOsebe==el[0]:
            return(el)
        
    
def osebaIzposojen():
    '''Funkcija bo vrnila seznam oseb, ki imajo izposojene knjige in stevilo izposojenih knjig'''
    sql = '''SELECT DISTINCT st_izkaznice, ime, priimek, COUNT(st_izkaznice)
    FROM izposoja
    JOIN oseba
    ON (id_osebe=st_izkaznice)
    GROUP BY st_izkaznice'''
    for el in con.execute(sql):
        print(el)

def osebaIzposojenTrenutno(ime =''):
    '''Funkcija bo vrnila seznam oseb, ki imajo izposojene knjige in stevilo izposojenih knjig'''
    sql = '''SELECT DISTINCT st_izkaznice, ime, priimek, COUNT(st_izkaznice)
    FROM izposoja
    JOIN oseba
    ON (id_osebe=st_izkaznice)
    WHERE datum_vracila is null
    GROUP BY st_izkaznice;'''
    sez = []
    for el in con.execute(sql):
        sez.append(el)
    return sez

def osebaIzposojenTrenutnoEdn(idOsebe):
    '''Funkcija bo vrnila seznam oseb, ki imajo izposojene knjige in stevilo izposojenih knjig'''
    sql = '''SELECT DISTINCT st_izkaznice, ime, priimek, COUNT(st_izkaznice)
    FROM izposoja
    JOIN oseba
    ON (id_osebe=st_izkaznice)
    WHERE datum_vracila is null
    GROUP BY st_izkaznice;'''
    sez = []
    for el in con.execute(sql):
        if idOsebe==el[0]:
            return el

def knjigaProsta(idKnjige):
    '''Funkcija bo preverila če je knjiga na zalogi'''
    sql = '''SELECT stevilo FROM knjige WHERE id = ?'''
    steviloVseh = con.execute(sql,[idKnjige]) #koliko teh kjig imamo
    try:
        st = steviloVseh.fetchone()[0]
    except Exception as napaka:
        return('Napačn naslov oziroma ni knjige')
    if st == None:
        return 0
    sql = '''SELECT COUNT(id_knjige) FROM izposoja WHERE id_knjige = ? and datum_vracila is NULL'''
    s = con.execute(sql,[idKnjige])
    s1 = s.fetchone()[0]
    rez = st-s1
    return rez

def izracunaZamudnino(rok, vracilo):
    '''izracuna zamudnino'''
    cena = 0.05
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
    return (razlika, znesek)

def zamudnina():
    '''izračuna zamudnino za vse osebe'''
    sql = '''SELECT id_osebe AS oseba,
       potek_izposoje,
       datum_vracila,
       id_knjige AS knjiga
  FROM izposoja
 WHERE datum_vracila > potek_izposoje or
       datum_vracila IS  NULL; 
        '''
    sez =[]
    for el in con.execute(sql):
        oseba, rok, vracilo, knjiga = el[0], el[1], el[2], el[3]
        rok1 = rok.split('-')
        v = datetime.now().date()
        r = date(int(rok1[0]),int(rok1[1]),int(rok1[2]))
        razlika = v-r
        razlika = razlika.days
        if razlika<0:
            pass
        else:
            razlika, znesek = izracunaZamudnino(rok, vracilo)
            sez.append([oseba, knjiga, razlika, znesek])
    return sez

def zamudninaOseba(idOsebe):
    '''izračuna zamudnino za posamezno izposojo'''
    sql = '''SELECT id_osebe AS oseba,
       potek_izposoje,
       datum_vracila,
       id_knjige AS knjiga
  FROM izposoja
 WHERE id_osebe = ?;
        '''
    try:
        for el in con.execute(sql, [idOsebe]):
            oseba, rok, vracilo, knjiga = el[0], el[1], el[2], el[3]
        razlika, znesek = izracunaZamudnino(rok, vracilo) 
        return (oseba, knjiga, razlika, znesek)
    except Exception as napaka:
        return('Ni zamudnine')

def izposoja(idOsebe, idKnjige):
    '''naredimo izposojo'''
    datumIzposoje = datetime.now().date()
    datumVracila = datumIzposoje + timedelta(days = 14)
    sql = '''INSERT INTO izposoja (id_osebe, id_knjige, datum_izposoje, potek_izposoje) VALUES (?,?,?,?)'''
    con.execute(sql,[idOsebe, idKnjige, datumIzposoje, datumVracila]).fetchone()
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
    sql = '''UPDATE izposoja SET datum_vracila =? WHERE id_osebe=? AND id_knjige=?'''
    con.execute(sql,[datumVracila,idOsebe,idKnjige])
    con.commit()

def rezervacijaKnjige(idOsebe, idKnjige):
    '''Oseba naredi rezarvacijo knjige'''
    datumRezervacije = datetime.now().date()
    sql = '''INSERT INTO rezervacija (id_osebe, id_knjige, kdaj) VALUES (?,?,?)'''
    con.execute(sql,[idOsebe, idKnjige, datumRezervacije])
    con.commit()

def opravljenaRezervacija(idOsebe,idKnjige):
    '''Rezervacija je bila zaključena'''
    sql = '''UPDATE rezervacija SET zakljucena =? WHERE id_osebe=? AND id_knjige=?'''
    con.execute(sql,[1,idOsebe,idKnjige])
    con.commit()

def poisciOsebo(ime,priimek):
    '''Poišče osebo'''
    sql = '''select st_izkaznice from oseba where ime=? and priimek=?;'''
    try:
        a = con.execute(sql,[ime,priimek]).fetchone()
        return a[0]
    except Exception as napaka:
        return('Osebe s tem imenom ni v bazi')

def poisciKnjigo(naslov):
    '''Poišče osebo'''
    sql = '''select id from knjige where naslov=?;'''
    try:
        a = con.execute(sql,[naslov]).fetchone()
        return a[0]
    except Exception as napaka:
        return('Knjige s tem imenom ni v bazi')
