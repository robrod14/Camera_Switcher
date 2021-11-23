# Camera_Switcher
Camera.py
This code will listen to keyboard input and determine when the user has pressed "1", "2", "esc", or some other button. Pressing of the numbers coincides with switching cameras (i.e "1" = camera 1...). When on of the numbers are selected a signal is sent across the network to a webserver. When somehting other than a number "1" or "2" is pressed then the signal is sent to the webserver to turn off. If the "esc" button is pressed then the program exits.

webserver.py
This program is running on two Raspberry Pi zero w's. When a signal is received from Camera.py (by visiting a URL on the webserver). The server will send a GPIO signal to the raspaberry py sending 5 volts to the connected apace vision light causing it to turn off or on based on which camera is hot.
