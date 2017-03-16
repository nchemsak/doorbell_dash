import picamera

IMG_WIDTH = 800
IMG_HEIGHT = 600
IMAGE_DIR = "/home/pi/Desktop/"
IMG = "snap.jpg"

def pic():   
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.hflip = True
    camera.brightness = 60
    camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    camera.capture(IMAGE_DIR + IMG)
    camera.close()
