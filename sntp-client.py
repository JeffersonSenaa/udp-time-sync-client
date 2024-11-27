import socket
import time
import struct
from datetime import datetime

NTP_SERVER = "pool.ntp.org" #Servidor NTP público
PORT = 123
TIMEOUT = 20
MSG_SNTP = b'\x1b' + 47 * b'\0'


def consultar_servidor_ntp():
    pass
        
for tentativa in range(2):
    resultado = consultar_servidor_ntp()
    if resultado:
        print(f'Data/hora: {resultado}')
        break
    else:
        print("Tentativa falhou. Segunda tentativa")
else:
        print("Data/hora: não foi possível contactar servidor")