from flask import Flask
from flask import render_template
import urllib, codecs
import subprocess, os

def baixa_e_converte(url):
    lei = url.split("/")[-1]
    if not os.path.isfile("data/" + lei):
        arquivo = open("data/" + lei, "w")
        print "Downloading " + lei
        arquivo.write(urllib.urlopen(url).read())
        arquivo.close()
    if not os.path.isfile("data/" + lei[0:-3] + 'txt' ):
        print "Converting..."
        subprocess.call(["pdftotext", "data/" + lei])
        print "Conversion complete!"
    return codecs.open("data/" + lei[0:-3] + 'txt', 'r', encoding='utf-8').read()

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/pl/<pl>")
def teste(pl):
    texto = baixa_e_converte("http://camaramunicipalsp.qaplaweb.com.br/iah/fulltext/leis/L" + pl + ".pdf")
    law = {
        "id" : pl,
        "body" : texto
    }
    return render_template('law.html', law=law)

if __name__ == "__main__":
    app.debug = True
    app.run()