from bottle import post, get, route, request, HTTPResponse
import uuid
import logging

import reader_service as readerService

@get('/read-sensor')
def read_sensonr():

    id = createCorrelationId()

    logging.info("received read request using id: %s", id)
    result = readerService.readHumiditySensor(id)

    if (result["isSuccess"]):
        response = buildSuccessView(result)
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