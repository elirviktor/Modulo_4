import serial
import time
from datetime import datetime

lala = serial.Serial('COM3', 115200)

time.sleep(2)
lala.flushInput()
lala.flushOutput()

while True:
    dato = lala.readline()
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" tmp c: "+str(dato))
lala.close()
