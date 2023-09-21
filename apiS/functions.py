import pickle
import pandas as pd
import xgboost

def hacer_prediccion(datos):
    print(datos.head())
    # Cargar el modelo entrenado desde un archivo pickle
    with open('../dataModeling/modelo_definiivo.pkl', 'rb') as archivo_modelo:
        modelo = pickle.load(archivo_modelo)

    # Realizar la predicción utilizando el modelo
    prediccion = modelo.predict(datos)

    return prediccion


def inputDataModel(victAge, victSex, victRace, mesDelito, franjaHoraria):
    df = pd.read_csv('../data/datos_entrada_modelo_ejemplo.csv', sep=';')
    df['victAge'] = victAge
    df['victSex'] = victSex
    df['victRace'] = victRace
    df['mesDelito'] = mesDelito
    df['franjaHoraria'] = franjaHoraria
    print(df.head())
    return df


def buscar_peligrosidadTest(victAge, victSex, victRace, mesDelito, franjaHoraria):
    # Obtener los datos del formulario enviado
    # datos = request.form['datos_usuario']
    datos = inputDataModel(victAge, victSex, victRace, mesDelito, franjaHoraria)

    # Llamar a la función de predicción
    resultado_prediccion = hacer_prediccion(datos)
    resultado_prediccion.to_csv('../data/resultPredict.csv', index=False)


def getColor(zipcode):
    df = pd.read_csv('../data/resultPredict.csv', sep=',')
    # df = pd.read_csv('../data/resultadosPonderados.csv', sep=',')

    # print(df[df['ZipCode'] == zipcode])

    nivel = df[df['ZipCode'] == zipcode]['NivelPeligrosidad']
    print(nivel.iloc[0])
    return nivel

if __name__ == '__main__':
    print()
    # inputDataModel()
    buscar_peligrosidadTest("23", "M", "African", "08", "4")
    # getColor(90005)
