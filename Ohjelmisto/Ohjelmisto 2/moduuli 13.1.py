from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkulukutesti/<luku>/')
def alkuluku(luku):
    try:
        luku = int(luku)
        tilakoodi = 200
        if luku <= 1:
            vastaus = {
                "status" : tilakoodi,
                "Teksti" : f"{luku} ei ole alkuluku"
            }
        else:
            on_alkuluku = True
            for i in range(2, int(luku ** 0.5) +1):
                if luku % i == 0:
                    on_alkuluku = False
                    break
            if on_alkuluku:
                vastaus = {
                        "status" : tilakoodi,
                        "Teksti" : f"{luku} on alkuluku"
            }
            else:
                vastaus = {
                    "status" : tilakoodi,
                    "Teksti" : f"{luku} ei ole alkuluku"
                }




    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virhe"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)