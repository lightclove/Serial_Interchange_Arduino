import pytest

from serial_interchange.arduino_serial_client import ArduinoClient


@pytest.fixture
def arduino_client(debug_mode):
    client = ArduinoClient()
    client.connect()  # Устанавливаем соединение

    yield client

    # Закрываем соединение после завершения теста
    client.close()
