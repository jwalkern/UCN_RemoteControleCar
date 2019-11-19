"""
Dette er tcpServer, som modtager signal, og håndtere motor styring
"""

import socket
import RPi.GPIO as GPIO

# set motors ready for output
GPIO.setmode(GPIO.BCM)
chan_list = [16, 26, 12, 20, 21, 13]
GPIO.setup(chan_list, GPIO.OUT)


# define motor forwards and backwards
def rover_forward():
    GPIO.output(16, 0)
    GPIO.output(26, 1)
    GPIO.output(20, 1)
    GPIO.output(21, 0)


def rover_backward():
    GPIO.output(16, 1)
    GPIO.output(26, 0)
    GPIO.output(20, 0)
    GPIO.output(21, 1)


def pwm_power():
    l.ChangeDutyCycle(100)
    r.ChangeDutyCycle(100)


def pwm_power_stop():
    l.ChangeDutyCycle(0)
    r.ChangeDutyCycle(0)


def right():
    l.ChangeDutyCycle(45)
    r.ChangeDutyCycle(100)


def left():
    l.ChangeDutyCycle(100)
    r.ChangeDutyCycle(45)


print("Server is running.\n")
host = input("What is the server ip address?")
#host = "192.168.240.18"  # Dette er IP-adressen for Raspberry Pi
port = 3000  # Husk at portnumre på 1024 og lavere er priviligerede

skt = socket.socket()  # Man kan give argumenter til denne (f.eks. om det skal være TCP eller UDP)
skt.bind((host, port))  # Tilskriver IP-adressen og porten til vores socket

skt.listen()  # Lytter efter forbindelser
run = True
while run:
    forbindelse, addresse = skt.accept()
    print("Host with " + str(addresse[0]) + " are connected.")

    # turn on PWM
    l = GPIO.PWM(12, 300)
    r = GPIO.PWM(13, 300)
    l.start(0)
    r.start(0)

    runServer = True
    while runServer:
        data = forbindelse.recv(64)
        dekodet_data = data.decode("UTF-8")
        if dekodet_data == 'K_1':
            print('1')

        if dekodet_data == 'K_2':
            print('2')

        if dekodet_data == 'K_3':
            print('3')

        if dekodet_data == 'K_UP':
            print('up')
            rover_forward()
            pwm_power()

        if dekodet_data == 'K_DOWN':
            print('down')
            rover_backward()
            pwm_power()

        if dekodet_data == 'K_LEFT':
            print('left')
            rover_forward()
            left()

        if dekodet_data == 'K_RIGHT':
            print('right')
            rover_forward()
            right()

        if dekodet_data == 'K_SPACE':
            print('space')
            pwm_power_stop()

        if dekodet_data == 'K_ESCAPE':
            print('shutting server down')
            runServer = False
        # else:
        #    pwm_power_stop()

    forbindelse.close()
    GPIO.cleanup()
    run = False
skt.close()
