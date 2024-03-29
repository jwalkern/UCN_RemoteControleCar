"""
Dette er en TCP klient der håndtere Pygame, og sender det til vores TCP server som håndtere motorstyring.
Jan Nielsen
"""

import socket
import pygame

run = True
while run:
    skt = socket.socket()  # Laver en socket
    host = input("What is the server ip address? ")
    port = 3001
    skt.connect((host, port))

    pygame.init()
    screen = pygame.display.set_mode((50, 50))
    pygame.display.set_caption('Control window')

    # Access a needed loop for pygame commands
    pygameRun = True
    while pygameRun == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                skt.close()
                pygameRun = False
                pygame.quit()
        # Defining keys
        keys_pressed = pygame.key.get_pressed()
        # Ecs = quit
        if keys_pressed[pygame.K_ESCAPE]:
            data = 'K_ESCAPE'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        # Gear shift on rover
        if keys_pressed[pygame.K_1]:
            data = 'K_1'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_2]:
            data = 'K_2'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_3]:
            data = 'K_3'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)

        # Control the rover
        if keys_pressed[pygame.K_UP]:
            data = 'K_UP'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_DOWN]:
            data = 'K_DOWN'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_LEFT]:
            data = 'K_LEFT'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_RIGHT]:
            data = 'K_RIGHT'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)
        if keys_pressed[pygame.K_SPACE]:
            data = 'K_SPACE'
            indkodet_data = data.encode("UTF-8")
            skt.sendall(indkodet_data)


    skt.close()  # Lukker forbindelsen

    print("Bye")
    run = False