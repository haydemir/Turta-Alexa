from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)



def getTemp():
	degrees = sensor.read_temperature()
	return round(degrees,2)

def getHum():
	humidity = sensor.read_humidity()
	return round(humidity,2)


def relayCommand(relay,cmd):
	if relay == "1":
		relay = 20
	else:
		relay = 12

	GPIO.output(relay,cmd)
