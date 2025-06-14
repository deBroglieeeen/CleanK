from scservo_sdk import *
import time, sys

PORT      = '/dev/tty.wchusbserial5A460832611'   
BAUD      = 115200
ID        = 1
PROTOCOL  = 0                           # SCSCL = 0

def deg2pos(deg):              # 度→12bit 0-4095
    return int(deg * 4096 / 360) & 0x0FFF

port = PortHandler(PORT)
pkt  = PacketHandler(PROTOCOL)

if not port.openPort():
    sys.exit('open failed')
port.setBaudRate(BAUD)

# ① 0° → 90° → 180° を 0.6 秒ずつ
for ang in (0, 90, 180, 90, 0):
    pos = deg2pos(ang)
    # WRITE 指令：アドレス 0x2A (目標角) に角度と時間[ms]
    pkt.write2ByteTxRx(port, ID, 0x2A, pos)         # 角度
    pkt.write2ByteTxRx(port, ID, 0x2C, 600)         # 時間
    time.sleep(0.7)

port.closePort()
print('done')
