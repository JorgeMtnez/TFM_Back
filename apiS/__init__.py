from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from functions import hacer_prediccion

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/test', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type'])
def index():
    url = request.args.get('url')
    return " --> FUNCIONA" + str(url)


@app.route('/getColor', methods=['GET'])
@cross_origin()
def coloring():  # only for testingz
    print("im here")
    zicode = request.args.get('zipcode')
    if zicode == "90027":
        return {"data": "6ac728"}
    elif zicode == "90007":
        return {"data": "e9fc17"}
    elif zicode == "90006":
        return {"data": "fcb717"}
    elif zicode == "90005":
        return {"data": "fc6b17"}
    elif zicode == "90004":
        return {"data": "fc1717"}
    else:
        return {"data": "fc1717"}
    # return " --> FUNCIONA" + str(url)


@app.route('/buscar_peligrosidad', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type'])
def buscar_peligrosidad():
    # Obtener los datos del formulario enviado
    datos = request.form['datos_usuario']

    # Llamar a la función de predicción
    resultado_prediccion = hacer_prediccion(datos)

    # Devolver la predicción al frontend en formato JSON
    return jsonify({'prediccion': resultado_prediccion})


if __name__ == '__main__':
    app.run(debug=True)
