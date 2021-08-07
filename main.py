import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/tempo-populer')
def detik_populer():
    url = requests.get('https://www.tempo.co/populer')
    bs = BeautifulSoup(url.text, 'html.parser')

    contents = bs.find_all('div', attrs={'class': 'card card-type-1'})

    return render_template('tempo-populer.html', contens=contents)

@app.route('/idr-rates')
def idr_rates():
    base_url = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = base_url.json()
    return render_template('idr-rates.html', datas = json_data.values())


if __name__ == '__main__':
    app.run(debug=True)