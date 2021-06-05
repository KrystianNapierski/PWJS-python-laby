import sqlite3

conn = sqlite3.connect('database.db')
print("BazaDanych otwarta")

conn.execute('CREATE TABLE pracownicy (imie TEXT,nazwisko TEXT, nrpracownika TEXT, adres TEXT)')
print("Tabela utworzona")

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nrpracownika,adres) VALUES(?,?,?,?)",('Mateusz', 'Kowalski','1','Ogrodowa 11 Elblag') )
cur.execute('SELECT * FROM pracownicy ORDER BY nazwisko')
print(cur.fetchall())
conn.close()
print("BazaDanych zamknieta")
