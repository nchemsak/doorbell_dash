import picamera
import datetime

IMG_WIDTH = 800
IMG_HEIGHT = 600
#IMAGE_DIR = "/doorbell_dash_project/photos/photos"
IMAGE_DIR = "/home/pi/Desktop/"
IMG = "snap.jpg"
#suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S.jpg")
#file = "_".join([IMAGE_DIR, suffix])


def pic():
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.hflip = True
    camera.brightness = 60
    camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    camera.capture(IMAGE_DIR + IMG)
    #camera.capture(file)
    camera.close()



