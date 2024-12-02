import socket
import struct
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

NTP_SERVER = "pool.ntp.org" #Servidor NTP público
PORT = 123
TIMEOUT = 20
MSG_SNTP = b'\x1b' + 47 * b'\0'
# Calcula a diferença entre as épocas SNTP (1900) e Unix (1970)
EPOCH_SNTPS_TO_UNIX = (datetime(1970, 1, 1, tzinfo=timezone.utc) - datetime(1900, 1, 1, tzinfo=timezone.utc)).total_seconds()

def interpretar_resposta(data):
    # Extrai o timestamp transmitido (txTm_s) - começa no byte 40
    txTm_s = struct.unpack("!12I", data)[10] 
    timestamp = txTm_s - EPOCH_SNTPS_TO_UNIX  
    return datetime.fromtimestamp(timestamp, timezone.utc).astimezone(ZoneInfo("America/Sao_Paulo")).strftime('%a %b %d %H:%M:%S %Y')

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
        print("Tentativa falhou. Segunda tentativa...")
else:
        print("Data/hora: não foi possível contactar servidor")