import socket
import threading
import os
import sys

LOCAL_IP = "0.0.0.0"
LOCAL_PORT = int(os.getenv("LOCAL_PORT", 5000))

TARGET_IP = os.getenv("TARGET_IP")
TARGET_PORT = int(os.getenv("TARGET_PORT", 5000))

if not TARGET_IP:
    print("❌ ERROR: TARGET_IP is not set. Check your .env file.")
    sys.exit(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LOCAL_IP, LOCAL_PORT))
print(f"✅ Listening on port {LOCAL_PORT}, sending to {TARGET_IP}:{TARGET_PORT}")


def receive_messages():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\n📩 Message from {addr}: {data.decode()}")


def send_messages():
    while True:
        message = input("You: ")
        sock.sendto(message.encode(), (TARGET_IP, TARGET_PORT))


threading.Thread(target=receive_messages, daemon=True).start()
send_messages()