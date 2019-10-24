import os
import RPi.GPIO as GPIO
import pygame
import picamera

#set motors ready for output
GPIO.setmode(GPIO.BCM)
chan_list = [16,26,12,20,21,13]
GPIO.setup(chan_list, GPIO.OUT)
#define motor forwards and backwards
def rover_forward():
    GPIO.output(16,1)
    GPIO.output(26,0)
    GPIO.output(20,0)
    GPIO.output(21,1)
def rover_backward():
    GPIO.output(16,0)
    GPIO.output(26,1)
    GPIO.output(20,1)
    GPIO.output(21,0)
def pwm_power_start():
    l.ChangeDutyCycle(100)
    r.ChangeDutyCycle(100)
def pwm_power_stop():
    l.ChangeDutyCycle(0)
    r.ChangeDutyCycle(0)    
def take_picture():
    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.capture('/home/pi/Pictures/image.jpg')
    camera.close()
def pwm_power_state():
    pass
    

promt = ""
while promt != 'exit':
    os.system('cls||clear')
    promt = input("Type 'start' to start the motor.\nUse arrow keys to controle the Rover\nPress 'space' to break\nType 'exit' to stop motor.")
    if promt == 'start':
        #turn on PWM
        l = GPIO.PWM(12,300)
        r = GPIO.PWM(13,300)
        l.start(0)
        r.start(0)
        
        #turn on display and init camera
        pygame.init()
        screen = pygame.display.set_mode(800,600)
        pygame.display.set_caption('Rover CAM')

        #Access a needed loop for pygame commands
        run = True
        while run == True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False           
            #Defining keys
            keys_pressed = pygame.key.get_pressed() 
            #Ecs = quit
            if keys_pressed[pygame.K_ESCAPE]:
                run = False
                pygame.quit()            
            
            #Controlling rover
        if keys_pressed[pygame.K_UP]:
            rover_forward()
            pwm_power_start()
            print('up')
        if keys_pressed[pygame.K_DOWN]:
            rover_backward()
            pwm_power_start()
            print('down')
        if keys_pressed[pygame.K_LEFT]:
            rover_forward()
            l.ChangeDutyCycle(100)
            r.ChangeDutyCycle(50)
            print('left')             
        if keys_pressed[pygame.K_RIGHT]:
            rover_forward()
            l.ChangeDutyCycle(50)
            r.ChangeDutyCycle(100)
            print('right')
            
            #smile to the camera!! xD    
            if keys_pressed[pygame.K_1]:
                take_picture()
                print('snap_shot')
            
            #Space stops rover
            if keys_pressed[pygame.K_SPACE]:
                pwm_power_stop()
                print('chane boolean')
        pygame.display.quit()
        l.stop()
        r.stop()
        promt = ""
        continue
    elif promt == 'exit':
        break             
GPIO.cleanup()