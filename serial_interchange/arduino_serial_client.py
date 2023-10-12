from typing import Optional

import serial

from serial_interchange.rs485 import RS485Settings


class ArduinoClient:
    def __init__(
            self,
            serial_port: str = "/dev/ttyACM0",
            baud_rate: int = 9600,
            rs485_mode: bool = False,
            timeout: int = 3,
    ):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.rs485_mode = rs485_mode
        self.connection: Optional[serial.Serial] = None

    def connect(self) -> None:
        if self.serial_port is None or self.baud_rate is None:
            raise ValueError("Serial port and baud rate must be specified.")
        try:
            self.connection = serial.Serial(self.serial_port, self.baud_rate, timeout=self.timeout)
            if self.rs485_mode in ("True", "true", True, "1", 1):
                # Задаем настройки RS-485, далее используем обычную комманд send().
                # self.connection.baudrate = 9600  # set Baud rate to 9600
                # self.connection.bytesize = 8  # Number of data bits = 8
                # self.connection.parity = 'N'  # No parity
                # self.connection.stopbits = 1  # Number of Stop bits =
                # Включаем режим RS-485 (полудуплексный режим)
                self.connection.rs485_mode = RS485Settings()

        except Exception as e:
            raise ConnectionError(f"Failed to connect to {self.serial_port}: {str(e)}")

    def send_command(self, command: str) -> None:
        if not self.connection:
            raise ConnectionError("Not connected to Arduino. Call 'connect' method first.")
        try:
            self.connection.write(f"{command}\n".encode())
        except Exception as e:
            raise ConnectionError(f"Failed to send command: {str(e)}")

    def receive_response(self) -> str:
        if not self.connection:
            raise ConnectionError("Not connected to Arduino. Call 'connect' method first.")
        try:
            response = self.connection.readline().decode().strip()
            return response
        except Exception as e:
            raise ConnectionError(f"Failed to receive response: {str(e)}")

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None

    def __enter__(self) -> "ArduinoClient":
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


if __name__ == "__main__":
    with ArduinoClient() as arduino_client:
        arduino_client.send_command("\n")  # Отправляем символ "\n", иначе первая команда будет пропущена
        response = arduino_client.receive_response()
        print(response)
        arduino_client.send_command("WRONG")
        response = arduino_client.receive_response()
        print(response)
        arduino_client.send_command("LED_ON")
        response = arduino_client.receive_response()
        print(response)
        arduino_client.send_command("LED_OFF")
        response = arduino_client.receive_response()
        print(response)
