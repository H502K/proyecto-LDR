## ldr
import serial
import time

ser = serial.Serial('COM7', 9600)
time.sleep(2)

print("Leyendo datos del LDR...")

while True:
    linea = ser.readline().decode('utf-8').strip()
    print(f"Luz: {linea}%")


