import io
import os
import RPi.GPIO as GPIO
import pygame
import picamera

#set motors ready for output
GPIO.setmode(GPIO.BCM)
chan_list = [16,26,12,20,21,13]
GPIO.setup(chan_list, GPIO.OUT)
#define motor forwards and backwards
def left_forward():
    GPIO.output(16,1)
    GPIO.output(26,0)
def left_backward():
    GPIO.output(16,0)
    GPIO.output(26,1)
def right_forward():
    GPIO.output(20,0)
    GPIO.output(21,1)
def right_backward():
    GPIO.output(20,1)
    GPIO.output(21,0)
def pwm_power_start():
    l.ChangeDutyCycle(100)
    r.ChangeDutyCycle(100)
def pwm_power_stop():
    l.ChangeDutyCycle(0)
    r.ChangeDutyCycle(0)    
def take_picture():
    camera.capture('/home/pi/Pictures/image.jpg')
    
def camera_test():    
    #stream camera
    stream = io.BytesIO()
    camera.vflip = True
    camera.hflip = True
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:(camera.resolution[0]*camera.resolution[1]*3)],camera.resolution, 'RGB')
    screen.fill(0)
    if img:
        screen.blit(img,(x,y))            
    pygame.display.update()

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
        screen = pygame.display.set_mode((0,0))
        camera = picamera.PiCamera()
        camera.resolution = (1280, 720)
        camera.crop = (0.0, 0.0, 1.0, 1.0)
        pygame.display.set_caption('Rover CAM')
    
        x = (screen.get_width() - camera.resolution[0])/2
        y = (screen.get_height() - camera.resolution[1])/2
        
        rgb = bytearray(camera.resolution[0] * camera.resolution[1]*3)
    
        #Access a needed loop for pygame commands
        run = True
        while run == True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False           
            camera_test()
            #Defining keys
            keys_pressed = pygame.key.get_pressed() 
            #Ecs = quit
            if keys_pressed[pygame.K_ESCAPE]:
                run = False
                pygame.quit()            
            #Controlling rover
            if keys_pressed[pygame.K_UP]:
                left_forward()
                right_forward()
                pwm_power_start()
            if keys_pressed[pygame.K_DOWN]:
                left_backward()
                right_backward()
                pwm_power_start()
            if keys_pressed[pygame.K_LEFT]:
                right_forward()
                left_forward()
                l.ChangeDutyCycle(100)
                r.ChangeDutyCycle(50)                
            if keys_pressed[pygame.K_RIGHT]:
                left_forward()
                right_forward()
                l.ChangeDutyCycle(50)
                r.ChangeDutyCycle(100)
            
            #smile to the camera!! xD    
            if keys_pressed[pygame.K_1]:
                take_picture()
            
            #Space stops rover
            if keys_pressed[pygame.K_SPACE]:
                pwm_power_stop()
                
            
        camera.close()
        
        pygame.display.quit()
        l.stop()
        r.stop()
        promt = ""
        continue
    elif promt == 'exit':
        break             
GPIO.cleanup()