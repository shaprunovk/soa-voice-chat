import socket
import pyaudio
import threading

from chat_config import config
from chat_commands import client_commands

HOST = config.HOST
PORT = config.PORT

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
connection_close_status = False
mode_status = 'keyboard'

chunk_size = 1024
audio_format = pyaudio.paInt16
channels = 1
rate = 20000

# Mic use init
p = pyaudio.PyAudio()
playing_stream = p.open(
    format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size, start=True
)
recording_stream = p.open(
    format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size, start=False
)


def receive():
    global connection_close_status
    while True:
        if connection_close_status:
            exit(0)
        try:
            data = client.recv(1024)

            if mode_status == "keyboard":
                message = data.decode("utf-8")
                if not message:
                    continue
                if message == "Username":
                    client.send(nickname.encode("utf-8"))
                else:
                    print(message)
        except UnicodeDecodeError:
            playing_stream.write(data)
        except:
            connection_close_status = True
            client.close()
            break


def write():
    global mode_status, connection_close_status
    while True:
        if connection_close_status:
            exit(0)
        msg_text = input('')
        if msg_text in (client_commands.RECORD, client_commands.KEYBOARD):
            if msg_text == client_commands.RECORD:
                recording_stream.start_stream()
            else:
                recording_stream.stop_stream()
            mode_status = msg_text.replace("/", "")
            continue
        if msg_text and mode_status == "keyboard":
            message = f"{nickname}: {msg_text}"
            client.send(message.encode("utf-8"))
            if msg_text == client_commands.EXIT:
                connection_close_status = True
                client.close()
                exit(0)


def record():
    global connection_close_status
    while True:
        if connection_close_status:
            exit(0)
        try:
            if mode_status == "record":
                data = recording_stream.read(1024)
                client.sendall(data)
        except:
            connection_close_status = True
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

record_thread = threading.Thread(target=record)
record_thread.start()
