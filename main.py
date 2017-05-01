import serial
from time import sleep
import requests
import httplib

def initializeModule():
    global connection 
    print "Arduino Communication Module"
    print "Initializing..."
    while True:
        try:
            arduinoSerial = serial.Serial( "/dev/ttyACM0", baudrate=9600 )
            break;
        except Exception as e:
            print "Error opening socket with arduino. Trying again"
            sleep(5)
    return arduinoSerial
    

def sendMessageToCCM():
    try:
        connection = httplib.HTTPConnection("localhost", 3000)
        connection.request("GET","/api/camera/trigger-camera")
        response = connection.getresponse()
        print response.status, response.reason, response.read()
        connection.close()
    except Exception as e:
        print e

def monitorSensor(arduinoSerial):
    while True:
	try:
        	x = int(arduinoSerial.readline())
        	print "Detected Violation"
		if(x == 1):
		    sendMessageToCCM()
	except Exception as e:
		print e
connection = 0
arduinoSerial = initializeModule()
monitorSensor(arduinoSerial)
