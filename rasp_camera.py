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
    #camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    
    camera.start_preview()
    camera.annotate_text = "Doorbell pressed!"
    camera.annotate_text_size = 50
    #display video for 5 seconds
    sleep(5)
    camera.stop_preview()
    camera.close()


# https://www.raspberrypi.org/learning/tweeting-babbage/worksheet/


######################################################
# picamera default values:
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
# video will record 5 seconds
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
#             loop over camera effects:
######################################################
#camera = picamera.PiCamera()
#camera.vflip = True
#camera.hflip = True
#camera.start_preview()
#for effect in camera.IMAGE_EFFECTS:
#     camera.image_effect = effect
#     camera.annotate_text = "Effect: %s" % effect
#     sleep(1)
#camera.stop_preview()

