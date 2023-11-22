from modelo_analyzer.modelo2 import ClasificadorTexto

def predecir():

    clasificador = ClasificadorTexto()
    texto_a_predecir = "fuck"
    prediccion = clasificador.predecir(texto_a_predecir)
    print("Predicción:", prediccion)
