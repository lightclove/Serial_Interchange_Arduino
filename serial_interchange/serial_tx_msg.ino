/*
Arduino скетч для создания сервера, принимающего команды управления через Serial порт (COM порт)
ожидает команды от клиента Python через Serial порт. 
Клиент Python может отправлять команды "LED_ON" и "LED_OFF", 
чтобы управлять встроенным светодиодом на плате Arduino. 
Команды обрабатываются на Arduino, и ответы отправляются через Serial порт.
*/
void setup() {
  Serial.begin(9600); // Настройка скорости обмена данными через Serial порт
  pinMode(LED_BUILTIN, OUTPUT); // Настраиваем встроенный светодиод на выход
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Читаем команду от Serial порта
    command.trim(); // Удаляем лишние пробелы и символы новой строки

    // Обработка команды
    if (command == "LED_ON") {
      digitalWrite(LED_BUILTIN, HIGH); // Включаем встроенный светодиод
      Serial.println("LED включен");
    } else if (command == "LED_OFF") {
      digitalWrite(LED_BUILTIN, LOW); // Выключаем встроенный светодиод
      Serial.println("LED выключен");
    } else {
      Serial.println("Неверная команда"); // Отправляем сообщение об ошибке
    }
  }
}