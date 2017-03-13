#!/usr/bin/python

# this Python application turns a Raspberry Pi into a security camera system
# it requires that you have a Pi camera installed and an imgur account setup
# you also need to create an imgur application
# Written by Mike Haldas
# Detailed documentation about this project here: http://www.cctvcamerapros.com/Pi-Alarm-MMS
# Email me at mike@cctvcamerapros.net if you have questions
# You can also reach me @haldas on twitter or +Mike Haldas on Google+
# If you make any improvements to this code or use it in a cool way, please let me know

import re
import pyimgur
import time
import picamera
import RPi.GPIO as GPIO
from twilio.rest import TwilioRestClient

# define the GPIO port you will use for the door sensor
SENSOR = 19

# number of seconds to delay between alarm and snapshot
# in case you want to wait a second or two for the person to enter the room after triggering the sensor
DELAY = 5

#setup GPIO using Broadcom SOC channel numbering
GPIO.setmode(GPIO.BCM)

# set to pull-up (normally closed position for a door sensor)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# put your Twilio credentials here
ACCOUNT_SID = ""
AUTH_TOKEN = ""

# make sure to use format with +1 for USA #s. E.G +12463338910
TO_PHONE = ""
FROM_PHONE = ""

# text message to send with photo
TXT_MSG = "Door Alarm Triggered!"

# directory to save the snapshot in
IMAGE_DIR = "/var/www/"

# imgur client setup
CLIENT_ID = ""

# name and dimentsions of snapshot image
IMG = "snap.jpg"
IMG_WIDTH = 800
IMG_HEIGHT = 600

# initalize the Twilio client
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# initialize imgur client
im = pyimgur.Imgur(CLIENT_ID)

try:
    # setup an indefinite loop that looks for the door sensor to be opened
    while True:

        GPIO.wait_for_edge(SENSOR, GPIO.RISING)
        print("Door Opened!\n")
        time.sleep(DELAY)
        with picamera.PiCamera() as camera:
            camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
            camera.capture(IMAGE_DIR + IMG)

        uploaded_image = im.upload_image(IMAGE_DIR + IMG, title=TXT_MSG)
        client.messages.create(
            to=TO_PHONE,
            from_=FROM_PHONE,
            body=TXT_MSG,
            media_url=uploaded_image.link,
        )
finally:
    GPIO.cleanup() # ensures a clean exit
