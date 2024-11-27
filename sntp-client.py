import socket
import time
import struct
from datetime import datetime

NTP_SERVER = "pool.ntp.org" #Servidor NTP público
PORT = 123
TIMEOUT = 20
MSG_SNTP = b'\x1b' + 47 * b'\0'


def consultar_servidor_ntp():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(TIMEOUT)
            try:
                s.sendto(MSG_SNTP, (NTP_SERVER, PORT))
                data, _ = s.recvfrom(1024)
                return data
            except socket.timeout:
                return None
        
for tentativa in range(2):
    resultado = consultar_servidor_ntp()
    if resultado:
        print(f'Data/hora: {resultado}')
        break
    else:
        print("Tentativa falhou. Tentando novamente...")
else:
        print("Data/hora: não foi possível contactar servidor")