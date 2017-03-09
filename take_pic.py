import cv2
import datetime

def pic():
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)

    def get_image():
        retval, im = camera.read()
        return im
    for i in range(ramp_frames):
        temp = get_image()

    camera_capture = get_image()

    ##################################################################
    # Using datetime, name the photo with a unique file name
    ##################################################################
    basename = "images/doorbell"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S.jpg")
    file = "_".join([basename, suffix])

    cv2.imwrite(file, camera_capture)

    del(camera)
