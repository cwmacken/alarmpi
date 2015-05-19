<h3>Working Notes. Look for a decent write up in the future</h3>

Hello these are my edits to skiwithpete's repo located at https://github.com/skiwithpete/alarmpi

Here's the link to the youtube video https://www.youtube.com/watch?v=julETnOLkaU

special thanks to 2006Wicket for helping me make changes to my to the alarm config routes
  
  "For example, get_weather_yahoo.py has a line "config.read('alarm.conf')" which I changed to           "config.read('/home/pi/alarmpi/alarm.config')"
  
  
Also I found I needed to use sudo crontab -e to call my files rather than crontab -e


Powered By : http://www.spitcast.com/

Great setup article: http://lanhed.se/raspberry-pi-setup/

^ if you follow the above steps do your dev and git commits from ~/raspberyPi on your local after sshfs'ing and run your tests from a termial running ssh.



Happy Hacking

-Conor 
