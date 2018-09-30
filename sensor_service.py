import logging
import datetime
import random

import pi_client as piClient
import temp_reader as tempReader


def readHumiditySensor(correlationId):

    logging.info("id: %s -> performing a reading from humidity sensor", correlationId)

    try:
        value = performSensorReading(correlationId)

        return buildReadSuccessResponse(correlationId, value)
    
    except ValueError as ex:

        logging.error("id: %s -> can't read from sensor: %s", correlationId, ex)
        return buildErrorResponse(correlationId, "can't read from sensor")

def operateWaterPump(correlationId, action):

    logging.info("id: %s -> performing operation: %s water pump", correlationId, action)

    try:
        performActionWaterPump(correlationId, action)

        return buildSuccessAction(correlationId)

    except ValueError as ex:

        logging.error("id: %s -> can't perform operation: %s water pump -> %s", correlationId, action, ex)
        return buildErrorResponse(correlationId, "can't perform action: " + action + " water pump")

# temporary logic for sensor reading
def performSensorReading(correlationId):

    try:
        moisturePercentage = piClient.readMoisturePercentageLevel()
        logging.info("id: %s -> humidity: %s", correlationId, moisturePercentage)
        return moisturePercentage    

    except ValueError as ex:
        logging.error("id: %s -> can't read from sensor: %s", correlationId, ex)
        raise ValueError("can't read from sensor")


# temporary function while actuators work
def performActionWaterPump(correlationId, action):

    logging.info("id: %s -> perform action: %s water pump", correlationId, action)



def buildErrorResponse(correlationId, message):

    return {
        "isSuccess": False,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "message": message
    }

def buildReadSuccessResponse(correlationId, humidityValue):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "humidity": humidityValue
    }

def buildSuccessAction(correlationId):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
    }
