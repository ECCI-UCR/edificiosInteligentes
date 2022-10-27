from grovepi import *
ultrasonicoIzquierda = 3
ultrasonicoDerecha = 4

while True:
    distanciaIzquierda = ultrasonicRead(ultrasonicoIzquierda)
    distanciaDerecha = ultrasonicRead(ultrasonicoDerecha)
    print(distanciaIzquierda,',',distanciaDerecha)