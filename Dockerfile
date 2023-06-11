FROM python:latest

COPY ./chat-server.py .
COPY ./chat_commands.py .
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "chat_server.py"]
