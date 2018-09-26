import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 1
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# ADC input channel for Analog output
CHANNEL = 5

MAX_VALUE = 1024

def readMoistureRawLevel():
    return mcp.read_adc(CHANNEL)

def readMoisturePercentageLevel():
    percentage = ( (MAX_VALUE - readMoistureRawLevel()) / MAX_VALUE ) * 100

    return round(percentage, 2)


