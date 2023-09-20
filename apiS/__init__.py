from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from functions import hacer_prediccion

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/test', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type'])
def index():
    url = request.args.get('url')
    return " --> FUNCIONA" + str(url)

@app.route('/getColor', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type'])
def index():
    zicode = request.args.get('zipcode')
    if zicode == "90027":
        return "#c99d24"
    elif zicode == "90007":
        return "#fafa64"
    elif zicode == "90006":
        return "#a0c29b"
    elif zicode == "90005":
        return "#2892c7"
    elif zicode == "90004":
        return "#e81014"
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