from grovepi import *
ultrasonicoIzquierda = 3
ultrasonicoDerecha = 4

distanciaPorDefecto = 200

void leerDistancias()
    distanciaIzquierda = leerIzquierda()
    distanciaDerecha = leerDerecha()

int leerIzquierda()
    return ultrasonicRead( ultrasonicoIzquierda )

int leerDerecha()
    return ultrasonicRead( ultrasonicoDerecha )

bool cambioEnSensor()
    if ((distanciaIzquierda < distanciaPorDefecto) or (distanciaDerecha < distanciaPorDefecto)):
        return True
    return False

#TODO: 
'''
    en caso que se haga solo con distancias y no con tiempo, se veria a traves de
    un int si la interferencia esta en el sensor izquierdo o derecho. cuando este sea 0, es que el
    bloqueo ya paso (ambos sensores estan en distanciaPorDefecto) y, usando cual interferencia
    vino primero, se incrementa o decrementa el contador de personas

'''

while True:
    distanciaIzquierda = leerIzquierda()
    distanciaDerecha = leerDerecha()
    while (!cambioEnSensor())
        distanciaIzquierda = leerIzquierda()
        distanciaDerecha = leerDerecha()
        
    int interferenciaIzqOrDer+= interferenciaEnSensor()
    primeraInterferencia = determinarPrimeraInterferencia(interferenciaIzqOrDer)
    if (!cambioEnSensor):
        cantidadPersonas+= (cambiarNumeroDePersonas(interferencia))
        
        
    
