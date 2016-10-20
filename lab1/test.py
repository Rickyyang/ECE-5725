import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO22_callback(channel):
	cmd = 'echo "1111"'
	subprocess.call(cmd,shell=True)
	
