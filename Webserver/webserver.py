from flask import Flask
from flask import request
import time

app = Flask(__name__)

def turn_off():
    print(f'sending power once')
    print(f'sending power twice')
    print(f'sending power thrice')

def turn_on():
    print(f'sending power once')

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

@app.route("/api/v1/2")
def camera_two():
    turn = request.args.get('Turn')
    if turn == 'off':
        turn_off()
    elif turn == 'on':
        turn_on()

    return "<p>You sent command to cammera 2 </p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
