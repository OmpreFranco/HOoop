class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amp = amplitud
        self.ti = tiempo_inicial
        self.tf = tiempo_final
        #TODO: completar con la inicializacion de los parametros del objeto
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        ret = [senal[i]/4.0 for i in range(len(senal))]
        return ret
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        pass
