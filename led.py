import time
import RPi.GPIO as io # using RPi.GPIO

io.setmode(io.BCM)
io.setup(17,io.OUT) # make pin into an output

print("LED blinker - By Mike Cook")
print("Ctrl C to quit")

while True:
  io.output(17, 0)
  time.sleep(1)
  io.output(17, 1)
  time.sleep(1)

