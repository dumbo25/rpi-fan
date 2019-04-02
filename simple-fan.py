#!/susr/bin/python

# connect red lead to one pint to 3.3v pin (pin 1)
# connect black lead to GPIO 4 (pin 7)

# on NEMS run
# $ sudo apt-get install python-rpi.gpio python3-rpi.gpio -y

#########################
#
# simple-fan turns a fan on and off when temperature exceeds temperature
# thresholds.
#
# The fan comes with a MiuZei case, and can run on 3.3V (low speed) or
# 5V (high speed). The fan can be plugged into either 3.3V or 5.5v GPIO
# pin and to a ground GPIO pin, but that means the fan will always run
# and that isn't very much fun. Any fan can be used as long it can operate
# at 3.3V
#
# run-fan was tested on a raspberry pi 3b+ running nems linux
#
#########################

#########################
#
# simple-fan.py is based on:
#    https://stackoverflow.com/questions/41819683/how-can-i-control-a-fan-with-gpio-on-a-raspberry-pi-3-using-python
#
#########################

#########################
#
# simple-fan starts automatically using systemd
#
# Create a systemd service file using:
#   $ sudo nano /lib/systemd/system/simple-fan.service
#
# with the contents as shown below
# remove # and leading spaces:
#   [Unit]
#   Description=run fan when hot
#   After=meadiacenter.service
#
#   [Service]
#   # If User and Group are not specified as root, then it won't work
#   User=root
#   Group=root
#   Type=simple
#   ExecStart=/usr/bin/python /home/pi/run-fan.py
#   Restart=Always
#
#   [Install]
#   WantedBy=multi-user.target
#
# end of the simple-fan.service
# ctrl-o, ENTER, ctrl-x to save and exit the nano editor
#
# After any changes to /lib/systemd/system/simple-fan.service:
#    sudo systemctl daemon-reload
#    sudo systemctl enable simple-fan.service
#    sudo reboot
#
# Ensure the run-fan.service in systemd is enabled and running:
#    systemctl list-unit-files | grep enabled
#    systemctl | grep running | grep fan
#    systemctl status simple-fan.service -l
#
# If there are any issues with starting the script using systemd,
# then examine the journal using:
#    sudo journalctl -u simple-fan.service
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while True:     # Loop forever

    # Read the current temperature
    res = os.popen('vcgencmd measure_temp').readline()
    temp = float((res.replace("temp=","").replace("'C\n","")))

    # print 'Temperature from vcgencmd: {}'.format(temp)

    # Control the fan
    if temp > 65.0:
        # print 'Turning on GPIO 4'
        GPIO.output(4, False)
    else:
        # print 'Turning off GPIO 4'
        GPIO.output(4, True)

    # Wait before the next iteration
    sleep(10)

