from flask import Flask
from flask import request
import time
import RPi.GPIO as GPIO

i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Output_PIN = 23

GPIO.setup(Output_PIN, GPIO.OUT)
print('Starting up the PIR Module')
print('Ready')

app = Flask(__name__)

def turn_off():
    GPIO.output(Output_PIN, GPIO.LOW)
    print(f'sending power')

def turn_on():
    GPIO.output(Output_PIN, GPIO.HIGH)
    print(f'sending power')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/v1/camera")
def camera_one():
    turn = request.args.get('Turn')
    if turn == 'off':
        turn_off()
    elif turn == 'on':
        turn_on()

    return "<p>You sent command to camera 1 </p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
