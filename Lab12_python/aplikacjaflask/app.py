from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/about")
def about_me():
    dane = {'tytul':'O mnie','tresc':'Nazywam sie Napierski Krystian.'}
    return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])
@app.route("/info")
def information():
    posty = [{
    'author': {'username': 'Janek'},
    'body': 'Słonecznie w Elblągu!'
    },
    { 
    'author': {'username': 'Kasia'},
    'body': 'Film Kroll ma ciekawa fabule.'
    }]
    dane = {'tytul':'Informacje','tresc':'Informacje dotyczące mojej osoby.'}
    return render_template('informacje.html', tytul=dane['tytul'], tresc=dane['tresc'],posty=posty)
if __name__ == "__main__":
    app.run()   