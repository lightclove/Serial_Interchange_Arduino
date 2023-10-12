import os

from dotenv import load_dotenv

load_dotenv()

SERIAL_PORT = os.environ.get("SERIAL_PORT")
SERIAL_BAUDRATE = os.environ.get("SERIAL_BAUDRATE")
SERIAL_TIMEOUT = os.environ.get("SERIAL_TIMEOUT")
SERIAL_RS485_MODE = os.environ.get("SERIAL_RS485_MODE")
