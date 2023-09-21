from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)

@app.route("/")
def opendata():
    raw = {}
    res = []
    with urllib.request.urlopen("https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193") as url:
      raw = json.load(url)
    for data in raw['records']:
      if '2023-09-21' in data['fields']['bm_heure']:
        res.append({
            'bm_heure': data['fields']['bm_heure'],
            'bm_prevision': data['fields']['bm_prevision']
         })
    return render_template('app.html', data=res)