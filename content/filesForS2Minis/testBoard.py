import analogio as aio
import board
import time

ADCMAX = 2**16-1
DACREF = 3.3

adcTest = aio.AnalogIn(board.IO15)  # create an ADC object for pin 15

adcfactor = adcTest.reference_voltage/ADCMAX # factor to convert values to volts
dacfactor = ADCMAX/3.3

dac = aio.AnalogOut(board.IO17)

header = "vout,vtest,time"

data = []

dac.value = 0  # set dac low

print("sleeping.... let C discharge")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0 --- go!")

t0 = time.monotonic_ns()

for i in range(0,20):
    vout = i*3.3/20 # compute a voltage based on the loop count
    dac.value = int(dacfactor*vout)
    time.sleep(0.1)
    value = adcTest.value
    data.append((vout, value, time.monotonic_ns()-t0))
    print("vout: ", vout, "raw value:", value)

print("done!")

dac.value = 0 # give the LED a rest....

print(header)

for i in range(len(data)):
    vout, val, t = data[i] # get data for ith iteration
    print(f"{vout},{val*adcfactor},{t/1e9}")
    
