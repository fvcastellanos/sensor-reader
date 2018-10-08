import RPi.GPIO as io # using RPi.GPIO

PIN17 = 17

def setupPinOut(pinNumber):
    io.setmode(io.BCM)
    io.setup(pinNumber, io.OUT) # make pin into an output

def activateRelay():
    io.output(PIN17, 1)

def deactivateRelay():
    io.output(PIN17, 0)

