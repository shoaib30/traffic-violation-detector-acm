import serial
from time import sleep
import requests
import httplib

def initializeModule():
    global connection 
    print "Arduino Communication Module"
    print "Initializing..."
    
    arduinoSerial = serial.Serial( "/dev/ttyACM0", baudrate=9600 )
    return arduinoSerial
    

def sendMessageToCCM():
    connection = httplib.HTTPConnection("localhost", 3000)
    connection.request("GET","/api/camera/trigger-camera")
    response = connection.getresponse()
    print response.status, response.reason, response.read()
    connection.close()

def monitorSensor(arduinoSerial):
    while True:
        x = int(arduinoSerial.readline())
        print "Detected Violation"
        if(x == 1):
            sendMessageToCCM()
connection = 0
arduinoSerial = initializeModule()
monitorSensor(arduinoSerial)
