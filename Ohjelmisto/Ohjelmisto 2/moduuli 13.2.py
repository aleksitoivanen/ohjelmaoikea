from flask import Flask, Response
import json, mysql.connector

app = Flask(__name__)
@app.route('/kentta/<icao>/')
def etsi(icao):

    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Allu8221!',
        autocommit=True
    )
    sql = """
          SELECT ident, name, municipality
          FROM airport
          WHERE ident = %s \
          """

    cursor = yhteys.cursor()
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
    else:
        vastaus = {"error": "ICAO-koodia ei löytynyt"}

    return Response(json.dumps(vastaus, ensure_ascii=False),
                    mimetype="application/json")


if __name__ == "__main__":
    app.run( port=3000)
