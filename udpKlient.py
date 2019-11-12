# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:15:36 2018

Eksempel med klient. Dette kører en klient proces, etablerer
forbindelser til en server proces og sender noget data.
Derefter lukkes forbindelsen.
Der er ingen feedback fra server til klient i denne version.

@author: HTH
"""

import socket, time
import picamera
import io


print("Kører klienten\n")

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Laver en socket

host = "192.168.1.111"  # Dette er IP-adressen for Raspberry Pi
port = 3001


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    img = Image.fromarray(image,'RGB')
    output = StringIO.StringIO()
    img.save(output, format='JPEG')
    contents = output.getvalue()
    output.close()

    skt.sendto(contents, (host, port))
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
skt.close

print("Socketen blev lukket")