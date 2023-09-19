app = Flask(__name__)

@app.route('/buscar_peligrosidad', methods=['POST']) 
def buscar_peligrosidad():
    # Obtener los datos del formulario enviado
    datos = request.form['datos_usuario']

    # Llamar a la función de predicción
    resultado_prediccion = hacer_prediccion(datos)

    # Devolver la predicción al frontend en formato JSON
    return jsonify({'prediccion': resultado_prediccion})

if _name_ == '__main__':
    app.run()
def hacer_prediccion(datos):
    # Cargar el modelo entrenado desde un archivo pickle
    with open('C:\\Users\\amari\\Documents\\TFM Final\\modelo_ejecutable.pkl', 'rb') as archivo_modelo:
        modelo = pickle.load(archivo_modelo)

    # Realizar la predicción utilizando el modelo
    prediccion = modelo.predict(datos)

    return prediccion