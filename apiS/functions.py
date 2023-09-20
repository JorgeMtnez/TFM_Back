import pickle


def hacer_prediccion(datos):
    # Cargar el modelo entrenado desde un archivo pickle
    with open('../dataModeling/modelo_definiivo.pkl', 'rb') as archivo_modelo:
        modelo = pickle.load(archivo_modelo)

    # Realizar la predicción utilizando el modelo
    prediccion = modelo.predict(datos)

    return prediccion