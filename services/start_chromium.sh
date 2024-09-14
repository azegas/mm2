# Add the script to autostart:
# sudo vi /etc/xdg/lxsession/LXDE-pi/autostart
# Add this line at the end:
# @/home/arvypi/GIT/mm2/services/start_chromium.sh


# since service will alrady be running, we just launch chromium and it should work?
#!/bin/bash
export DISPLAY=:0
sleep 5
chromium-browser --start-fullscreen http://localhost:5000