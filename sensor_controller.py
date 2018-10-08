from bottle import post, get, route, request, HTTPResponse
import uuid
import logging

import sensor_service as readerService

@get('/soil-sensor')
def read_humidity_sensor():

    id = createCorrelationId()

    logging.info("received read request using id: %s", id)
    result = readerService.readHumiditySensor(id)

    if (result["isSuccess"]):
        response = buildSuccessHumidityView(result)
        return HTTPResponse(status=200, body=response)
    
    error = buildErrorView(result)
    return HTTPResponse(status=422, body=error)

@get('/temperature-sensor')
def read_temperature_sensor():

    id = createCorrelationId()

    logging.info("received read temperature request using id: %s", id)
    result = readerService.readTemperatureSensor(id)

    if (result['isSuccess']):
        response = buildSuccessTemperatureView(result)
        return HTTPResponse(status=200, body=response)

    error = buildErrorView(result)
    return HTTPResponse(status=422, body=error)

@post('/water-pump')
def water_pump():

    id = createCorrelationId()

    logging.info("received a water pump request using id: %s", id)

    # body = request.json
    # action = body['action']
    action = request.json.get('action')

    result = readerService.operateWaterPump(id, action)

    if (result['isSuccess']):
        
        response = buildSuccessActionView(result)
        return HTTPResponse(status=200, body=response)

    error = buildErrorView(result)
    return HTTPResponse(status=422, body=error)

def createCorrelationId():
    return str(uuid.uuid1())

def buildErrorView(response):
    return {
        "correlationId": response["correlationId"],
        "message": response["message"]
    }

def buildSuccessHumidityView(response):
    return {
        "correlationId": response["correlationId"],
        "humidity": response["humidity"]
    }

def buildSuccessTemperatureView(response):
    return {
        "correlationId": response["correlationId"],
        "temperature": response["temperature"]
    }

def buildSuccessActionView(response):
    return {
        "correlationId": response["correlationId"]
    }
