import pickle
import pandas as pd
import xgboost

def hacer_prediccion(datos):

    print("/////////////////")
    # Cargar el modelo entrenado desde un archivo pickle
    with open('../dataModeling/finalPickel.pkl', 'rb') as archivo_modelo:
        modelo = pickle.load(archivo_modelo)

    # Realizar la predicción utilizando el modelo
    prediccion = modelo.predict(datos)
    data = []
    newDf = pd.DataFrame(data)
    df = pd.read_csv('../data/datos_entrada_modelo_ejemplo.csv', sep=';')
    newDf['zipcode'] = df['ZipCode']
    newDf['nivel'] = prediccion

    return newDf


def inputDataModel(victAge, victSex, victRace, mesDelito, franjaHoraria):
    df = pd.read_csv('../data/datos_entrada_modelo_ejemplo.csv', sep=';')
    df['VictAge'] = int(victAge)
    df['VictSex'] = victSex
    df['VictRace'] = victRace
    df['MesDelito'] = int(mesDelito)
    df['Franja_Horaria'] = int(franjaHoraria)
    print('/////////////////////')
    df['VictRace'] = df['VictRace'].replace(['Asian'], 1)
    df['VictRace'] = df['VictRace'].replace(['North American'], 2)
    df['VictRace'] = df['VictRace'].replace(['African'], 3)
    df['VictRace'] = df['VictRace'].replace(['Latin American'], 4)
    df['VictRace'] = df['VictRace'].replace(['UNK'], 5)

    df['VictSex'] = df['VictSex'].replace(['M'], 1)
    df['VictSex'] = df['VictSex'].replace(['F'], 2)
    df['VictSex'] = df['VictSex'].replace(['X'], 3)

    print(df.head())
    print(df.info())
    print(list(df))
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


mapeo_VictRace = {'Asian': 1 ,'North American' : 2,'African' : 3,'Latin American' : 4,'Otros' : 5}

if __name__ == '__main__':
    print()
    # inputDataModel("23", "M", "African", "08", "4")
    # print(hacer_prediccion(inputDataModel("23", "M", "African", "08", "4")))

    hacer_prediccion(inputDataModel("23", "M", "African", "08", "4")).to_csv('../data/resultPredict.csv', index=False)
    # getColor(90005)
