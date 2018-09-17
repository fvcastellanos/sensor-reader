from bottle import post, get, route, request, HTTPResponse, request
import uuid
import logging

import sensor_service as readerService

@get('/soil-sensor')
def read_sensonr():

    id = createCorrelationId()

    logging.info("received read request using id: %s", id)
    result = readerService.readHumiditySensor(id)

    if (result["isSuccess"]):
        response = buildSuccessView(result)
        return HTTPResponse(status=200, body=response)
    
    error = buildErrorView(result)
    return HTTPResponse(status=422, body=error)

@post('/pump')
def water_pump():

    id = createCorrelationId()

    logging.info("received a water pump request using id: %s", id)

    body = request.json
    action = body['action']

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

def buildSuccessView(response):
    return {
        "correlationId": response["correlationId"],
        "humidity": response["humidity"],
        "temperature": response["temperature"]
    }

def buildSuccessActionView(response):
    return {
        "correlationId": response["correlationId"]
    }