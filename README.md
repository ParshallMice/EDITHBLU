# EDITHBLU

To set up the Raspberry Pi to work as smart glasses type this into the command line:
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
If the file doesnt exist make it exist.

At the top of the file write:
sudo python [the path to the clock.py starting with "/home/pi/"]
