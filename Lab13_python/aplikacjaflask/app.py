from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)
conn = sql.connect('database.db')
conn.execute('DROP TABLE praacownicy')
conn.execute('CREATE TABLE praacownicy(imie TEXT, nazwisko TEXT, nrpracownika TEXT, adres TEXT)')
conn.close()

@app.route("/")
def main():
    return render_template('glowna.html')


@app.route("/dodaj")
def new_pracownik():
    return render_template('dodaj.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            imie = request.form['imie']
            nazwisko = request.form['nazwisko']
            nrpracownika = request.form['nrpracownika']
            adres = request.form['adres']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO praacownicy(imie, nazwisko, nrpracownika,adres) VALUES(?,?,?,?)",
                            (imie, nazwisko, nrpracownika, adres))
            con.commit()
            msg = "Rekord zapisany"
        except:
         con.rollback()
         msg = "Blad przy dodawaniu rekordu"
        
        finally:
         return render_template("rezultat.html",msg = msg)
         con.close()
        
@app.route('/lista')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM praacownicy ORDER BY imie,nazwisko')
    rekordy = cur.fetchall()
    return render_template("lista.html", rekordy=rekordy)


if __name__ == "__main__":
    app.run()



