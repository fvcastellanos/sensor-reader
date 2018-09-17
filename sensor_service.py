import logging
import datetime
import random

def readHumiditySensor(correlationId):

    logging.info("id: %s -> performing a reading from humidity sensor", correlationId)

    try:
        value = performSensorReading(correlationId)

        return buildReadSuccessResponse(correlationId, value["humidity"], value["temperature"])
    
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

    temperature = random.sample([15, 20, 25, 10, -5, 40], 1)
    humidity = random.sample([15, 20, 25, 10, -5, 40], 1)

    logging.info("id: %s -> temperature: %s - humidity: %s", correlationId, temperature, humidity)

    if ((temperature[0] == -5) or (humidity[0] == -5)):

        logging.error("id: %s -> can't read from sensor", correlationId)
        raise ValueError("can't read from sensor")

    return {
        "humidity": humidity[0],
        "temperature": temperature[0]
    }

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

def buildReadSuccessResponse(correlationId, humidityValue, temperatureValue):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "humidity": humidityValue,
        "temperature": temperatureValue
    }

def buildSuccessAction(correlationId):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
    }
