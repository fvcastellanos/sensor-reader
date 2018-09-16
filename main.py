from bottle import run
import logging

import reader_controller

FORMAT = '%(asctime)s %(message)s'
DATE_FORMAT = '%Y/%m/%d %I:%M:%S %p'

logging.basicConfig(level = logging.INFO, format = FORMAT, datefmt = DATE_FORMAT)

logging.info("starting sensor reader application...")

run(host='0.0.0.0', port=8080)
