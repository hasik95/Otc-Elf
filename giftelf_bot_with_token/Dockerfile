FROM python:3.12

WORKDIR /app
COPY . .

# Устанавливаем системные зависимости
RUN apt update && \
    apt install -y gcc python3-dev libffi-dev libssl-dev build-essential && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "main.py"]
