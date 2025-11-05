#!/usr/bin/env python3
"""
WebSocket сервер для GPS трекера ATGM336H
Работает в любом браузере включая Firefox
"""

from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
import threading
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gps_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Глобальные переменные
ser = None
is_connected = False

def read_gps_data():
    """Чтение данных с GPS модуля в отдельном потоке"""
    global ser, is_connected
    
    while True:
        try:
            if ser and ser.is_open:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line.startswith('$'):
                        # Отправляем данные всем подключенным клиентам
                        socketio.emit('gps_data', {'nmea': line})
                        print(f"Sent: {line}")
            time.sleep(0.01)
        except Exception as e:
            print(f"Ошибка чтения: {e}")
            time.sleep(1)

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index_websocket.html')

@socketio.on('connect')
def handle_connect():
    """Обработка подключения клиента"""
    global is_connected
    is_connected = True
    print("Клиент подключен")
    socketio.emit('connection_status', {'status': 'connected', 'message': 'Подключено к GPS модулю'})

@socketio.on('disconnect')
def handle_disconnect():
    """Обработка отключения клиента"""
    global is_connected
    is_connected = False
    print("Клиент отключен")

def init_serial_port(port='/dev/ttyUSB0', baudrate=9600):
    """Инициализация последовательного порта"""
    global ser
    try:
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1
        )
        print(f"Подключено к {port} на {baudrate} бод")
        return True
    except Exception as e:
        print(f"Ошибка подключения к {port}: {e}")
        return False

if __name__ == '__main__':
    # Попробуем разные порты
    ports_to_try = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0', '/dev/ttyS0']
    
    for port in ports_to_try:
        if init_serial_port(port):
            break
    else:
        print("Не удалось подключиться ни к одному порту")
        # Продолжим работу, но без GPS данных
    
    # Запускаем поток чтения данных
    if ser:
        thread = threading.Thread(target=read_gps_data, daemon=True)
        thread.start()
    
    # Запускаем веб-сервер
    print("Запуск веб-сервера на http://0.0.0.0:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

