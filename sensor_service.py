import logging
import datetime
import random

import pi_client as piClient
import temp_reader as tempReader
import relay_actuator as relayActuator


def readHumiditySensor(correlationId):

    logging.info("id: %s -> performing a reading from humidity sensor", correlationId)

    try:
        value = performMoistureSensorReading(correlationId)

        return buildReadHumiditySuccessResponse(correlationId, value)
    
    except ValueError as ex:

        logging.error("id: %s -> can't read from humidity sensor: %s", correlationId, ex)
        return buildErrorResponse(correlationId, "can't read from humidity sensor")

def readTemperatureSensor(correlationId):

    logging.info("id: %s -> performing a reading from temperature sensor", correlationId)

    try: 
        value = performTemperatureSensorReading(correlationId)

        return buildReadTemperatureSuccessResponse(correlationId, value)

    except ValueError as ex:

        logging.error("id: %s -> can't read from temperature sensor: %s", correlationId, ex)
        return buildErrorResponse(correlationId, "can't read from temperature sensor")

def operateWaterPump(correlationId, action):

    logging.info("id: %s -> performing operation: %s water pump", correlationId, action)

    try:
        performActionWaterPump(correlationId, action)

        return buildSuccessAction(correlationId)

    except ValueError as ex:

        logging.error("id: %s -> can't perform operation: %s water pump -> %s", correlationId, action, ex)
        return buildErrorResponse(correlationId, "can't perform action: " + action + " water pump")

def performMoistureSensorReading(correlationId):

    try:
        moisturePercentage = piClient.readMoisturePercentageLevel()
        logging.info("id: %s -> humidity: %s", correlationId, moisturePercentage)
        return moisturePercentage    

    except ValueError as ex:
        logging.error("id: %s -> can't read from humidity sensor: %s", correlationId, ex)
        raise ValueError("can't read from humidity sensor")


def performTemperatureSensorReading(correlationId):

    try:
        temperature = tempReader.read_temp()
        logging.info("id: %s -> temperature: %s", correlationId, temperature)
        return temperature

    except ValueError as ex:
        logging.error("id: %s -> can't read from temperature sensor: %s", correlationId, ex)
        raise ValueError("can't read from temperature sensor")

def performActionWaterPump(correlationId, action):

    logging.info("id: %s -> perform action: %s water pump", correlationId, action)
    if action == 1 :
        relayActuator.activateRelay()
    else :
        relayActuator.deactivateRelay()



def buildErrorResponse(correlationId, message):

    return {
        "isSuccess": False,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "message": message
    }

def buildReadHumiditySuccessResponse(correlationId, humidityValue):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "humidity": humidityValue
    }

def buildReadTemperatureSuccessResponse(correlationId, humidityValue):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "temperature": humidityValue
    }

def buildSuccessAction(correlationId):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
    }
