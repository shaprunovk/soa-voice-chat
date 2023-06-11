# soa-voice-chat
Voice chat on sockets
Не связан с игрой Мафия.

- **Локально**
  1. Установить необходимые пакеты
     ```
     pip3 install -r requirements.txt
     ```
  2. Отредактировать конфиг по пути ```chat_config.py``` (если требуется).
  3. Запустить:
     ```python3 chat_server.py```
- **Docker**
    - Собрать image
        ```
        docker build -t voice/chat . -f Dockerfile
        ```

    - Запустить собранный image в контейнере
        ```
        docker run -d -p ${YOUR_PORT}:${YOUR_PORT} --name voicechat -t voice/chat
        ```

Клиент запускается локально (Не работает на удаленной машине по SSH, так как библиотеке нужен доступ к микрофону):
 1. Установить необходимые пакеты
     ```
     pip3 install -r requirements.txt
     ```
 2. Запустить:
     ```python3 chat_client.py```

### Общение
По дефолту чат письменный, можно создавать комнаты, приглашать в них людей, в `chat_commands.py` написан список возможных команд.
Есть голосовой режим с `/record`. Изначально все подключившиеся находятся в одной комнате.


