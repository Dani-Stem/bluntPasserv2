from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
ask = Ask(app, '/')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)



GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2

servo1.start(0)
servo2.start(0)

@ask.launch
def start_skill():
    welcome_message = 'OK, OK!'

    x=1000

    for i in range(0, x):
        servo2.ChangeDutyCycle( 2.5 *(x-i)/x + 6.5 * i/x)
        time.sleep(0.001)
        
    time.sleep(1)

    for i in range(0, x):
        servo2.ChangeDutyCycle( 6.5 *(x-i)/x + 2.5 * i/x)
        time.sleep(0.001)
    time.sleep(1)
    return statement(welcome_message)



@app.route('/')
def homepage():
    return "Hi, there"


if __name__ == '__main__':
    app.run(port=5000, debug=True)



