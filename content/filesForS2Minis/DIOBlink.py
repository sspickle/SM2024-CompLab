print("Blinking with digital IO!")

import digitalio as dio
import board
import time

dout = dio.DigitalInOut(board.IO17)
dout.direction = dio.Direction.OUTPUT


while True:
    dout.value = 1
    time.sleep(0.2)
    dout.value = 0
    time.sleep(0.2)
    

