# run script as SUDO
# repurpose: ac:63:be:de:a0:63
# multivitamins: f0:27:2d:4a:96:a9
# wilsonjONes: 84:d6:d0:da:43:b4
# MilkBaby: 0c:47:c9:ac:35:56

# look at TWILIO for push notifications

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import cv2
import datetime


def arp_display(pkt):
    # url_pc = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=ENTER_YOUR_KEY_HERE&message='
    # url_mobile = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=ENTER_YOUR_KEY_HERE&message='

    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc:
            if pkt[ARP].hwsrc == 'f0:27:2d:4a:96:a9':
                print("smile..you pushed multivitamins")
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


            # elif pkt[ARP].hwsrc == 'ac:63:be:de:a0:63':
            #     # print("you dumbass. taking a picture to remember your failure...")
            #     print("smile, you pressed repurpose button")
            #     camera_port = 0
            #     ramp_frames = 30
            #     camera = cv2.VideoCapture(camera_port)
            #     def get_image():
            #         retval, im = camera.read()
            #         return im
            #     for i in range(ramp_frames):
            #         temp = get_image()

            #     camera_capture = get_image()
            #     file = 'IncorrectAnswer.jpg'
            #     cv2.imwrite(file, camera_capture)

            #     del(camera)


if __name__ == "__main__":
    sniff(prn=arp_display, filter="arp", store=0, count=0)


