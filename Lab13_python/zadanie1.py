import sqlite3

conn = sqlite3.connect('database.db')
cur=conn.cursor()
conn.execute('DROP TABLE praacownicy')
conn.execute('CREATE TABLE praacownicy(imie TEXT, nazwisko TEXT, nrpracownika TEXT, adres TEXT)')
cur.execute("INSERT INTO praacownicy(imie, nazwisko, nrpracownika,adres) VALUES(?,?,?,?)",('Paweł', 'Lasowy', '4', 'Grunwaldzka 13'))
cur.execute('SELECT * FROM praacownicy ORDER BY imie')
print(cur.fetchall())

