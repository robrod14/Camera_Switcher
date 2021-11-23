import paramiko
import requests

from paramiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError
from pynput import keyboard

camera1_ip = 'x.x.x.x' #'172.16.105.131'
camera2_ip = 'x.x.x.x'
username = 'username'
password = 'password'
cmd_to_execute = 'flask run'
camera1 = 'off'
camera2 = 'off'

def connect(server):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(server, username=username, password=password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
    except AuthenticationException as a_exc:
        print('Looks like there was an authentication error.')
    except NoValidConnectionsError as n_exc:
        print('Looks like the server is not up')


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
        if key.char == "1":
            camera1 = turn_camera_on(camera1_ip)
            if camera2 == 'on':
                camera2 = turn_camera_off(camera2_ip)
            print(f'\nCamera1 is {camera1}. Camera2 is {camera2}.')
            return True
        elif key.char == "2":
            camera2 = turn_camera_on(camera2_ip)
            if camera1 == 'on':
                camera1 = turn_camera_off(camera1_ip)
            print(f'\nCamera1 is {camera1}. Camera2 is {camera2}.')
            return True
        else:
            if camera1 == 'on':
                camera1 = turn_camera_off(camera1_ip)
            elif camera2 == 'on':
                camera2 = turn_camera_off(camera2_ip)
            print(f'\nCamera1 is {camera1}. Camera2 is {camera2}.')
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
print(f'Starting webserver on Camera 1')
#connect(camera1)
print(f'Camera 1 webserver started succesfully')
print(f'Starting webserver on Camera 2')
print(f'Camera 2 webserver started succesfully')
wait_for_user_input()