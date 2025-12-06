import serial
import threading
import time

port = "COM5"
baudrate = 115200

arduinocom = serial.Serial(port, baudrate, timeout=0.1)
time.sleep(2)

def send(message):
    arduinocom.write((f"Python Says: {message + '\n'}").encode('utf-8'))

def receive():
    if arduinocom.in_waiting > 0:
        received_data = arduinocom.readline().decode('utf-8').strip()
        if received_data:
            print(f"\nArduino says: {received_data}")

def continuous_received():
    while running:
        receive()
        time.sleep(0.1)

running = True
receiverThread = threading.Thread(target=continuous_received, daemon=True)
receiverThread.start()

while True:
    message = input("Message:")
    if message:
        send(message)

arduinocom.close()