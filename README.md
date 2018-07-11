# Turta-Alexa

[![Python 3.6](https://img.shields.io/pypi/v/python-symphony.svg)](https://www.python.org/downloads/release/python-360/)
![MIT](https://img.shields.io/pypi/l/ansicolortags.svg)

## Welcome to Turta-Alexa Skill.

## Getting Started

With this capability you will have chance to control your turta family with your voice over Alexa.
For detailed information about Turta family : https://www.turta.io

## Prerequisites

Install Paho-mqtt for python 2

```
pip install paho-mqtt
```
And if you need install RPi.GPIO

```
sudo apt-get update
sudo apt-get -y install python-rpi.gpio
```

### Installing


1- Go to Turta Alexa Certificate Generation web site [Turta Alexa Web](https://turtaalexa.com/).

and get your certificates by using Amazon Login 
(Detailed information about Amazon Login https://www.amazon.com/gp/help/customer/display.html?nodeId=201194060)

Turta-Alexa just uses your Amazon e-mail as "username" to reach your turta device.

2- After you get your certificates from your e-mail, download this repository and copy certificates to the directory you will run python_turta.py

  ## Directory structure should be like this
       -Adafruit_BME280.py
       -Adafruit_GPIO
       -python_alexa.py
       -turta_py.py
       -turta_mqtt_ca.crt
       -python_alexa_test.py
       -xxx.crt
       -xxx.key
       -README.md
      
3- Go to Alexa App, download Turta Skill App and register with your device.

### Running 

4- Run your code with your e-mail on raspberry as Turta equipped
```
  python python_turta.py -e "email" 
  
  if you want to test code and connection without raspberry pi
  use python python_turta_test.py -e "email"
  and then say commands to alexa and observer console logs
  ```
  
  
  ### Turta is ready for Alexa commands
    Alexa commands
  ```
  To activate turta: Alexa, open Turta
  
  To on/off relays: Alexa, turn off/on relay one/two
  
  To get temperature: Alexa, what is temperature?
  
  Or
  to command Turta directly
  
  Alexa, ask turta turn off/on relay one/two
  
  Alexa, ask turta what is temperature?
  ```
