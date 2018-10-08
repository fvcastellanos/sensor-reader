from bottle import run
import logging

import sensor_controller

import relay_actuator as relayActuator

FORMAT = '%(asctime)s %(message)s'
DATE_FORMAT = '%Y/%m/%d %I:%M:%S %p'

logging.basicConfig(level = logging.INFO, format = FORMAT, datefmt = DATE_FORMAT, filename = 'sensor-reader.log')

logging.info("starting sensor reader application...")

# do not like why I have to do it here...
# setting up pin 17 as ouput, turning off relay
relayActuator.setupPinOut(relayActuator.PIN17)
relayActuator.deactivateRelay()

run(host='0.0.0.0', port=8080)
