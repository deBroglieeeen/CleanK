from scservo_sdk import *
import sys

PORT = '/dev/tty.wchusbserial5A460832611'   # ←各自のポート名に
BAUD = 115200
ID   = 1
PROTOCOL = 0                       # STS/SC 系なら 0 (=SCSCL)

port = PortHandler(PORT)
pkt  = PacketHandler(PROTOCOL)

if not port.openPort():
    sys.exit('Port open failed')
port.setBaudRate(BAUD)

model, _, res = pkt.ping(port, ID)
if res == COMM_SUCCESS:
    print(f'Ping OK: model {model}')
else:
    print(f'Ping NG: result {res}')

port.closePort()
