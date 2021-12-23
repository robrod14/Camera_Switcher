import requests
from pynput import keyboard

GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
END = '\033[0m'
BOLD = '\x1b[1m'
RESET = '\x1b[21m'

camera1_ip = '10.1.10.93'  # '192.168.1.54'
camera2_ip = '10.1.10.138'  # '192.168.1.67'
cmd_to_execute = 'flask run'
camera1 = 'off'
camera2 = 'off'


def check_server_ready(ip_address):
    try:
        r = requests.get(f'http://{ip_address}:5000')
        if r.status_code == 200:
            return True
    except requests.exceptions.ConnectionError  as ce:
        print(f'{FAIL}Network problems;{END} {ce}.')
    except requests.exceptions.Timeout as to:
        print(f'{FAIL}Timeout Issues;{END} {to}.')


def turn_camera_on(ip_address):
    r = requests.get(f'http://{ip_address}:5000/api/v1/camera?Turn=on')
    camera = 'on'
    return camera


def turn_camera_off(ip_address):
    r = requests.get(f'http://{ip_address}:5000/api/v1/camera?Turn=off')
    camera = 'off'
    return camera


def on_press(key):
    global camera1
    global camera2

    try:
        if key.char == "1" and camera1 != "on":
            camera1 = turn_camera_on(camera1_ip)
            if camera2 == 'on':
                camera2 = turn_camera_off(camera2_ip)
            return True
        elif key.char == "2" and camera2 != "on":
            camera2 = turn_camera_on(camera2_ip)
            if camera1 == 'on':
                camera1 = turn_camera_off(camera1_ip)
            return True
        else:
            if camera1 == 'on' and key.char != "1":
                camera1 = turn_camera_off(camera1_ip)
            elif camera2 == 'on' and key.char != "2":
                camera2 = turn_camera_off(camera2_ip)
    except AttributeError:
        pass


def on_release(key):
    try:
        if key.char == '0':
            print(f"{WARNING}Shutting down...{END}")
            exit()
    except AttributeError:
        pass


def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()


print('Running Camera switcher')
print('Checking if Camera 1 is up and running')
if check_server_ready(camera1_ip):
    print(f"{GREEN}Camera 1 server is ready!{END}")
    camera1_ready = True
else:
    print(f"{WARNING}Camera 1 server is not ready. Please make sure the server is on or give it more time.{END}")
    camera1_ready = False
print('Checking if Camera 2 is up and running')
if check_server_ready(camera2_ip):
    print(f"{GREEN}Camera 2 server if ready!{END}")
    camera2_ready = True
else:
    print(f"{WARNING}Camera 2 server is not ready. Please make sure the server is on or give it more time.{END}")
    camera2_ready = False
if camera1_ready is False or camera2_ready is False:
    print(f"{FAIL}Shutting down. So you can fix the servers.{END}")
    exit()
else:
    print(f'Press {FAIL}{BOLD}"0"{RESET}{END} to close the program')
wait_for_user_input()
