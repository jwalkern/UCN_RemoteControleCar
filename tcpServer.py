"""
Dette er tcpServer, som modtager signal, og håndtere motor styring
"""

import socket

print("Kører serveren\n")

host = "192.168.240.18"  # Dette er IP-adressen for Raspberry Pi
port = 3000  # Husk at portnumre på 1024 og lavere er priviligerede

skt = socket.socket()  # Man kan give argumenter til denne (f.eks. om det skal være TCP eller UDP)
skt.bind((host, port))  # Tilskriver IP-adressen og porten til vores socket

antalForbindelser = int(input("Vælg antal forbindelser:"))

skt.listen()  # Lytter efter forbindelser
while antalForbindelser > 0:
    forbindelse, addresse = skt.accept()
    print("Værten med " + str(addresse[0]) + " har etableret forbindelse.")

    # Moodtager data
    while True:
        data = forbindelse.recv(64)

        dekodet_data = data.decode("UTF-8")

        if data:
            print("Data modtaget: ", str(dekodet_data))
        else:
            print("Ikke mere data.")
            break

    forbindelse.close()

    antalForbindelser = antalForbindelser - 1

skt.close()