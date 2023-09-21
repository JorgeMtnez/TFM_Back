from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
from functions import hacer_prediccion, inputDataModel, getColor

app = Flask(__name__)
# cors = CORS(app)
CORS(app, resources={r"/getColor": {"origins": "http://localhost:4200"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# @app.route('/getColor', methods=['GET'])
# def coloring():  # only for testingz
#     print("im here")
#     zicode = request.args.get('zipcode')
#     if zicode == "90027":
#         return {"data": "6ac728"}
#     elif zicode == "90007":
#         return {"data": "e9fc17"}
#     elif zicode == "90006":
#         return {"data": "fcb717"}
#     elif zicode == "90005":
#         return {"data": "fc6b17"}
#     elif zicode == "90003":
#         return {"data": "fc1717"}
#     else:
#         return {"data": "fc1717"}
#     # return " --> FUNCIONA" + str(url)

@app.route('/getColor', methods=['GET'])
def coloring():  # only for testingz
    print("im here")
    zicode = request.args.get('zipcode')
    nivel = getColor(zicode)
    if nivel == 1:
        return {"data": "6ac728"}
    elif nivel == 2:
        return {"data": "e9fc17"}
    elif nivel == 3:
        return {"data": "fcb717"}
    elif nivel == 4:
        return {"data": "fc6b17"}
    elif nivel == 5:
        return {"data": "fc1717"}
    else:
        return {"data": "fc1717"}
    # return " --> FUNCIONA" + str(url)


@app.route('/buscar_peligrosidad', methods=['GET'])
def buscar_peligrosidad():
    # Obtener los datos del formulario enviado
    # datos = request.form['datos_usuario']
    if request.args.get('victSex') == 'No comment':
        sex = 'X'
    else:
        sex = request.args.get('victSex')

    if request.args.get('victRace') == 'Other':
        raze = 'UNK'
    else:
        raze = request.args.get('victRace')

    if int(request.args.get('franjaHoraria')) >= 0 and int(request.args.get('franjaHoraria')) <= 6:
        franja = 4
    elif int(request.args.get('franjaHoraria')) > 6 and int(request.args.get('franjaHoraria')) <= 12:
        franja = 1
    elif int(request.args.get('franjaHoraria')) > 12 and int(request.args.get('franjaHoraria')) <= 16:
        franja = 2
    else:
        franja = 3


    datos = inputDataModel(
        request.args.get('victAge'),
        sex,
        raze,
        request.args.get('mesDelito'),
        franja
    )

    # Llamar a la función de predicción
    resultado_prediccion = hacer_prediccion(datos)
    resultado_prediccion.to_csv('../data/resultPredict.csv', index=False)

    # Devolver la predicción al frontend en formato JSON
    # return jsonify({'prediccion': resultado_prediccion})

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)
