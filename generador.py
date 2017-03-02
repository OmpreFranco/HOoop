"""
Un generador de senal es el responsable de generar una senal portadora.

"""

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math
        import numpy as np
        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(cantidad_muestras)
        #TODO agregar un ruido blanco a la senal
#==============================================================================
# Vamos a generar el ruido blanco
        
        
#==============================================================================

        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) + self.amplitud *np.random.uniform(-1,1)*0.001 \
        for i in muestras]

        return ret

#-------------------