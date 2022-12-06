import serial
import time
from datetime import datetime

archivo = open("temperatura.cvs", "w")
#lineab = ""

lala = serial.Serial('COM3', 115200)

time.sleep(2)
lala.flushInput()
lala.flushOutput()

i = int(input("ingrese cantidad de registros a reportar: "))
contador = 0

while contador < i:
    dato = lala.readline().decode('utf-8').rstrip()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linea2 = '{};{}'.format(fecha, dato) + '\n'
    archivo.write(linea2)
    contador += 1
lala.close()
archivo.close()
