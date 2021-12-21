import requests

from pynput import keyboard

camera1_ip = '10.1.10.93' #'172.16.105.131'
camera2_ip = '10.1.10.138'
cmd_to_execute = 'flask run'
camera1 = 'off'
camera2 = 'off'


def check_server_ready(ip_address):
    r = requests.get(f'http://{ip_address}:5000')
    if r.status_code != 200:
       return False
    else:
       return True

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
            #print(f'\nCamera1 is {camera1}. Camera2 is {camera2}. First print')
            return True
        elif key.char == "2" and camera2 != "on":
            camera2 = turn_camera_on(camera2_ip)
            if camera1 == 'on':
                camera1 = turn_camera_off(camera1_ip)
            #print(f'\nCamera1 is {camera1}. Camera2 is {camera2}. Second print')
            return True
        else:
            if camera1 == 'on' and key.char != "1":
                camera1 = turn_camera_off(camera1_ip)
            elif camera2 == 'on' and key.char != "2":
                camera2 = turn_camera_off(camera2_ip)
            #print(f'\nCamera1 is {camera1}. Camera2 is {camera2}. Third print {key.char} {type(key.char)}')
    except AttributeError as ex:
        print(ex)


def on_release(key):
    if key == keyboard.Key.esc:
        return False


def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join() 


print(f'Running Camera switcher')
print(f'Checking if Camera 1 is up and running')
if check_server_ready(camera1_ip):
   print(f"Camera 1 server is ready!")
else:
   print(f"Camera 1 server is not ready")
print(f'Checking if Camera 2 is up and running')
if check_server_ready(camera2_ip):
   print(f"Camera 2 server if ready!")
else:
   print(f"Camera 2 server is not ready!")
wait_for_user_input()
