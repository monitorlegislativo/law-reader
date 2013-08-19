from flask import Flask
from flask import render_template
import urllib
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
    return open("data/" + lei[0:-3] + 'txt', 'r').read()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pl/<pl>")
def teste(pl):
    texto = baixa_e_converte("http://camaramunicipalsp.qaplaweb.com.br/iah/fulltext/leis/" + pl + ".pdf")
    return "<pre>" + texto + "</pre>"

if __name__ == "__main__":
    app.debug = True
    app.run()