# rpi-fan
Raspberry Pi 3 Fan 

run-fan.py turns a fan on when CPU temperature exceeds a start temperature, and shuts the fan off when the temperature is below a stop temperature.

Any fan can be used. The fan's description/specifications should be:
  operates at 3.3V or operates in a range that includes 3.3V
  silent
  brushless

The fan I used came with a MiuZei case.

run-fan was tested on a raspberry pi running kodi on osmc using a 3.3v. However, it can be used on any Raspberry Pi by changing the service to use the correct username and copy run-fan.py to /home/username, instead of /home/osmc

There is an instructable that describes the setup in detail

run-fan.service should be copied to here: /lib/systemd/system/run-fan.service
run-fan.py should be copied to here: /home/osmc/run-fan.py
