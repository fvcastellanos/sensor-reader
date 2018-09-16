import logging
import datetime
import random

def readHumiditySensor(correlationId):

    logging.info("id: %s -> performing a reading from humidity sensor", correlationId)

    try:
        value = performSensorReading(correlationId)

        return buildSuccessResponse(correlationId, value["humidity"], value["temperature"])
    
    except ValueError as ex:

        logging.error("can't read from sensor: %s", ex)
        return buildErrorResponse(correlationId, "can't read from sensor")

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

def buildErrorResponse(correlationId, message):

    return {
        "isSuccess": False,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "message": message
    }

def buildSuccessResponse(correlationId, humidityValue, temperatureValue):
    return {
        "isSuccess": True,
        "time": datetime.datetime.now(),
        "correlationId": correlationId,
        "humidity": humidityValue,
        "temperature": temperatureValue
    }
