"""
Dette er en TCP klient der håndtere Pygame, og sender det til vores TCP server som håndtere motorstyring.
Jan Nielsen
"""

import socket
import pygame


promt = input("Type 'start' to connect server.")
if promt == 'start':
    run = True
else:
    print("shutting client down.")
    run = False

while run:
    skt = socket.socket()  # Laver en socket
    host = "192.168.1.111"  # Dette er IP-adressen for Raspberry Pi
    port = 3000
    skt.connect((host, port))

    pygame.init()
    screen = pygame.display.set_mode(800, 600)
    pygame.display.set_caption('Control window')

    # Access a needed loop for pygame commands
    pygameRun = True
    while pygameRun == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                skt.close()
                pygameRun = False
        # Defining keys
        keys_pressed = pygame.key.get_pressed()
        # Ecs = quit
        if keys_pressed[pygame.K_ESCAPE]:
            data = 'K_ESCAPE'
            indkodet_data = data.encode("UTF-8")
            pygameRun = False
            pygame.quit()
        # Gear shift on rover
        if keys_pressed[pygame.K_1]:
            print("Power at 30%")
            data = 'K_1'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_2]:
            print("Power at 60%")
            data = 'K_2'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_3]:
            print("Power at 100%")
            data = 'K_3'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)

        # Control the rover
        if keys_pressed[pygame.K_UP]:
            print('up')
            data = 'K_UP'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_DOWN]:
            print('down')
            data = 'K_DOWN'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_LEFT]:
            print('left')
            data = 'K_LEFT'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_RIGHT]:
            print('right')
            data = 'K_RIGHT'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)


    skt.close()  # Lukker forbindelsen

    print("Socketen blev lukket")