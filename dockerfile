FROM python:3.11-slim

WORKDIR /app

COPY udp_chat.py .

EXPOSE 5000/udp

CMD ["python", "udp_chat.py"]