import picamera
from time import sleep


IMG_WIDTH = 800
IMG_HEIGHT = 600
IMAGE_DIR = "/home/pi/Desktop/"
IMG = "snap.jpg"

def vid():   
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.hflip = True
    camera.brightness = 60
    camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    #camera.capture(IMAGE_DIR + IMG)
    


    camera.start_preview()
    camera.annotate_text = "Doorbell pressed!"
    camera.annotate_text_size = 50
    sleep(5)
    #camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    camera.close()


# camera = picamera.PiCamera()
# default brightness is 50
#camera.brightness = 70
#camera.capture('/home/pi/Desktop/image.jpg')

# https://www.raspberrypi.org/learning/tweeting-babbage/worksheet/


######################################################
# other picamera values:
######################################################
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 180
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)

######################################################
# video will record 5 seonds
######################################################
# camera.start_recording('video.h264')
# sleep(5)
# camera.stop_recording()

######################################################
#               add text to video:
######################################################
#camera.start_preview()
#camera.annotate_text = "Doorbell pressed!"
#camera.annotate_text_size = 50
#sleep(5)
#camera.capture('/home/pi/Desktop/text.jpg')
#camera.stop_preview()

######################################################
#                   loop over effects:
######################################################
#camera.start_preview()
#for effect in camera.IMAGE_EFFECTS:
#     camera.image_effect = effect
#     camera.annotate_text = "Effect: %s" % effect
#     sleep(5)
#camera.stop_preview()


######################################################
#                   tweet photos:
######################################################
# from picamera import PiCamera
# from time import sleep


# camera = PiCamera()

# camera.start_preview()
# sleep(3)
# camera.capture('/home/pi/image.jpg')
# camera.stop_preview()

# message = "Here's a Pi camera picture!"
# with open('/home/pi/image.jpg', 'rb') as photo:
#     twitter.update_status_with_media(status=message, media=photo)

######################################################
#               tweet with a datetime stamp on file name
######################################################
# from picamera import PiCamera
# from time import sleep
# from datetime import datetime

# timestamp = datetime.now().isoformat()
# photo_path = '/home/pi/tweeting-babbage/photos/%s.jpg' % timestamp

# camera = PiCamera()

# camera.start_preview()
# sleep(3)
# camera.capture(photo_path)
# camera.stop_preview()

# message = "Here's a Pi camera picture!"
# with open(photo_path, 'rb') as photo:
#     twitter.update_status_with_media(status=message, media=photo)





######################################################
# tweet with a datetime stamp on file name on button press
######################################################
# from twython import Twython
# from picamera import PiCamera
# from time import sleep
# from datetime import datetime
# from gpiozero import Button
# import random
# from auth import (
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret
# )

# twitter = Twython(
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret
# )

# button = Button(14)
# camera = PiCamera()

# messages = [
#     "Hello world",
#     "Hi there",
#     "My name is Babbage",
#     "What's up?",
#     "How's it going?",
#     "Have you been here before?",
#     "Get a hair cut!",
# ]

# while True:
#     button.wait_for_press()
#     message = random.choice(messages)
#     timestamp = datetime.now().isoformat()
#     photo_path = '/home/pi/tweeting-babbage/photos/%s.jpg' % timestamp
#     sleep(3)
#     camera.capture(photo_path)

#     with open(photo_path, 'rb') as photo:
#         twitter.update_status_with_media(status=message, media=photo)
