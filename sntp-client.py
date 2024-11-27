import socket
import time
import struct
from datetime import datetime

NTP_SERVER = "pool.ntp.org" #Servidor NTP público
PORT = 123
TIMEOUT = 20
MSG_SNTP = b'\x1b' + 47 * b'\0'

def interpretar_resposta(data):
    # Extrai o timestamp transmitido (txTm_s) - começa no byte 40
    txTm_s = struct.unpack("!12I", data)[10] 
    # Conversao de epoch SNTP (1900) para epoch Unix (1970)
    timestamp = txTm_s - 2208988800  
    return datetime.utcfromtimestamp(timestamp).strftime('%a %b %d %H:%M:%S %Y')

def consultar_servidor_ntp():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(TIMEOUT)
            try:
                s.sendto(MSG_SNTP, (NTP_SERVER, PORT))
                data, _ = s.recvfrom(1024)
                return interpretar_resposta(data)
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