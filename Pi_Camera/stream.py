'''
Dette modul er til stream
'''


  
def start_camera():
    
    import io
    import pygame
    import picamera
    
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
                   
        #smile to the camera!! xD    
        if keys_pressed[pygame.K_1]:
            take_picture()
                        
        
    camera.close()
    pygame.display.quit()          
