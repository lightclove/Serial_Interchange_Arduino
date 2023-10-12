import time

# Список команд для отправки
command = ("\n", "LED_ON", "LED_OFF", "Unknown")

# Ожидаемые ответы для каждой команды
expected_response = ("LED включен", "LED выключен", "Неверная команда")


# def test_connect(arduino_client):
#     arduino_client.connect()
#     assert arduino_client.connection is not None  # Проверяем, что соединение установлено
#     arduino_client.send_command(command[0])  # Отправляем символ "\n", иначе первая команда будет пропущена
#     response = arduino_client.receive_response()
#     try:
#         assert response == ""
#     except AssertionError:
#         print(f"Command: {command[1]}, Expected: {expected_response[0]}, Actual: {response}")
#         raise  # Повторно вызываем исключение AssertionError, чтобы оно было замечено Pytest
#
#
# def test_send_command(arduino_client):
#     arduino_client.connect()
#     arduino_client.send_command(command[1])  # "LED_ON"
#     time.sleep(3)
#     response = arduino_client.receive_response()
#     try:
#         assert response == command[1]  # "LED включен"
#     except AssertionError:
#         print(f"Command: {command[1]}, Expected: {expected_response[0]}, Actual: {response}")
#         raise
#
#
# def test_receive_response(arduino_client):
#     arduino_client.connect()
#     arduino_client.send_command("LED_OFF")
#     time.sleep(3)
#     response = arduino_client.receive_response()
#     try:
#         assert response == command[2]  # "LED выключен"
#     except AssertionError:
#         print(f"Command: {command[2]}, Expected: {expected_response[1]}, Actual: {response}")
#         raise


def test_send_multiple_commands(arduino_client):
    # Отправка команд и проверка ответов
    for c, er in zip(command[1:], expected_response[1:]):
        arduino_client.send_command(command)
        time.sleep(3)
        response = arduino_client.receive_response()
        try:
            assert response == expected_response
        except AssertionError:
            print(f"Response is: {response} and type of response is {type(response)}")
            print(f"Command: {command[2]}, Expected: {expected_response[1]}, Actual: {response}")
            raise

# Параметризированные тесты:
# @pytest.mark.parametrize("command, expected_response", [
#     ("\n", ""),
#     ("LED_ON", "LED включен"),
#     ("LED_OFF", "LED выключен"),
#     ("Unknown command", "Неверная команда")
# ])
# def test_send_multiple_commands(arduino_client, command, expected_response):
#     arduino_client.send_command(command)
#     response = arduino_client.receive_response()
#     try:
#         assert response == expected_response
#     except AssertionError:
#         print(f"Command: {command[2]}, Expected: {expected_response[1]}, Actual: {response}")
#         raise
