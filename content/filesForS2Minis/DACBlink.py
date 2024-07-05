print("Blinking with the DAC!")

import analogio as aio
import board
import time

dac = aio.AnalogOut(board.IO17)

while True:
    dac.value = 0xffff
    time.sleep(0.2)
    dac.value = 0
    time.sleep(0.2)
    

