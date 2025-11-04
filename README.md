# gps-tracker-atgm336h
A comprehensive web-based GPS tracking application for the ATGM336H GPS+BeiDou module with real-time mapping, data logging, and advanced analysis capabilities.

# GPS Tracker ATGM336H 🌍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Web Serial API](https://img.shields.io/badge/Web-Serial_API-blue.svg)]()
[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-green.svg)]()

Мощный трекер для GPS модуля ATGM336H с отображением на картах в реальном времени, ведением логов и расширенной аналитикой.

## 📋 Содержание

- [Возможности](#возможности)
- [Быстрый старт](#быстрый-старт)
- [Установка](#установка)
- [Использование](#использование)
- [Аппаратная настройка](#аппаратная-настройка)
- [Разработка](#разработка)
- [Лицензия](#лицензия)

## ✨ Возможности

- 🗺️ **Реальное время**: Отслеживание позиции на OpenStreetMap
- 📊 **Аналитика**: Статистика сообщений, качество сигнала, отслеживание ошибок
- 💾 **Логирование**: Настраиваемое хранение с автоматическим именованием
- 🔄 **Гибкий интерфейс**: Горизонтальный/вертикальный режимы
- ⚙️ **Настройки**: Размер буфера, скорость порта, обработка сообщений

## 🚀 Быстрый старт

### Веб-версия (рекомендуется)

# Клонируйте репозиторий
git clone https://github.com/yourusername/gps-tracker-atgm336h.git

cd gps-tracker-atgm336h

# Откройте в браузере
open index.html

GPS Tracker ATGM336H 🌍

English | Русский

## English

📡 GPS Tracker for ATGM336H Module

A comprehensive web-based GPS tracking application for the ATGM336H GPS+BeiDou module with real-time mapping, data logging, and advanced analysis capabilities.

https://img.shields.io/badge/GPS-Tracker-brightgreen
https://img.shields.io/badge/Web-Serial_API-blue
https://img.shields.io/badge/Maps-Leaflet-green

✨ Features

🌍 Real-time Mapping: Live position tracking with OpenStreetMap

📊 Advanced Statistics: Message analysis, signal quality, and error tracking

💾 Data Logging: Configurable log storage with automatic file naming

🔄 Dual Layout: Horizontal/vertical layout switching

⚙️ Configurable Settings: Buffer size, baud rate, and message handling

🔍 NMEA Analysis: Complete NMEA message parsing and validation

📈 Signal Quality: HDOP, satellite count, and fix quality monitoring

⏰ PPS Monitoring: Pulse-per-second signal tracking

🚀 Quick Start

Web Application (Recommended)

Clone the repository

bash

git clone https://github.com/yourusername/gps-tracker-atgm336h.git

cd gps-tracker-atgm336h

Open the application

Open index.html in Chrome/Edge 89+

Or serve via web server:

bash

python -m http.server 8000

# Then visit http://localhost:8000

Connect your GPS module

Click "Connect" button

Select your serial port (e.g., /dev/cu.usbserial-* on macOS)

View real-time data on the map!

Python Tools

bash

# Install dependencies

pip install pyserial pynmea2

# Run GPS monitor

python gps_monitor.py /dev/cu.usbserial-1420

# Analyze log files

python gps_analyzer.py gps_logs/your_log_file.txt

🛠️ Hardware Setup

Required Components

ATGM336H GPS module

USB to UART converter (CP2102, CH340, FT232, etc.)

GPS antenna

Jumper wires

Wiring Diagram

text

ATGM336H        USB-UART

VCC      →      3.3V/5V

GND      →      GND

TX       →      RX

RX       →      TX

PPS      →      (Optional) GPIO for hardware PPS

📁 Project Structure

text

gps-tracker-atgm336h/

├── index.html              # Main web application

├── gps_monitor.py          # Python monitoring tool

├── gps_analyzer.py         # Log analysis tool

├── config.py              # Configuration file

├── requirements.txt       # Python dependencies

└── gps_logs/             # Log directory (auto-created)

    ├── gps_trec_log_*.txt
    
    └── gps_data_*.txt

⚙️ Configuration

Web Application Settings

Baud Rate: 4800-115200 (default: 9600)

Buffer Size: 1KB-16KB (default: 4KB)

Log Lines: 10-1000 (default: 200)

Layout: Horizontal/Vertical

Supported NMEA Messages

$GNGGA, $GPGGA - GPS fix data

$GNRMC, $GPRMC - Recommended minimum data

$GNGSA, $GPGSA - GPS DOP and active satellites

$GPGSV, $BDGSV - Satellite information

$GPTXT - Text messages

🎯 Usage Examples

Real-time Tracking

Connect GPS module to computer

Open web application

Click "Connect" and select serial port

View your position on the map

Monitor satellite statistics and signal quality

Data Analysis

Record session using web app or Python script

Use analyzer to assess positioning stability:

bash

python gps_analyzer.py gps_logs/gps_data_20251103_182821.txt

Generate stability reports and accuracy assessments

🌟 Advanced Features

Signal Quality Assessment

HDOP-based accuracy circles on map

Satellite count with visual progress bar

Fix quality classification (None, 2D, 3D, DGPS, etc.)

PPS synchronization monitoring

Data Management

Automatic log rotation

Configurable buffer sizes

Truncated message handling

Export functionality with metadata

Cross-platform Compatibility

Web: Chrome 89+, Edge 89+

Python: 3.7+ with pyserial

OS: Windows, macOS, Linux

🐛 Troubleshooting

Common Issues

Web Serial not available

Use Chrome/Edge 89+

Enable #enable-experimental-web-platform-features in chrome://flags

Ensure HTTPS or localhost

No GPS data received

Check wiring (TX→RX, RX→TX)

Verify baud rate (usually 9600)

Ensure antenna has sky view

Check module power (3.3V/5V)

Truncated messages in logs

Increase buffer size in settings

Check baud rate compatibility

Ensure stable USB connection

🤝 Contributing

We welcome contributions! Please feel free to:

Report bugs and issues

Suggest new features

Submit pull requests

Improve documentation

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

Leaflet for amazing mapping library

OpenStreetMap for free map tiles

ATGM336H manufacturers for reliable GPS hardware

Web Serial API team for browser serial communication

## Русский

📡 GPS Трекер для модуля ATGM336H

Веб-приложение для отслеживания GPS с модулем ATGM336H (GPS+BeiDou) в реальном времени, ведением логов и расширенными возможностями анализа.

✨ Возможности

🌍 Карты в реальном времени: Отслеживание позиции на OpenStreetMap

📊 Расширенная статистика: Анализ сообщений, качество сигнала, отслеживание ошибок

💾 Ведение логов: Настраиваемое хранение с автоматическим именованием файлов

🔄 Двойной layout: Переключение между горизонтальным и вертикальным режимом

⚙️ Настраиваемые параметры: Размер буфера, скорость порта, обработка сообщений

🔍 Анализ NMEA: Полный парсинг и валидация NMEA сообщений

📈 Качество сигнала: HDOP, количество спутников, мониторинг качества фиксации

⏰ Мониторинг PPS: Отслеживание импульсов в секунду

🚀 Быстрый старт

Веб-приложение (Рекомендуется)

Склонируйте репозиторий

bash

git clone https://github.com/yourusername/gps-tracker-atgm336h.git

cd gps-tracker-atgm336h

Откройте приложение

Откройте index.html в Chrome/Edge 89+

Или запустите через веб-сервер:

bash

python -m http.server 8000

#### Затем откройте http://localhost:8000

Подключите GPS модуль

Нажмите кнопку "Подключиться"

Выберите последовательный порт (например, /dev/cu.usbserial-* на macOS)

Наблюдайте данные в реальном времени на карте!

Python инструменты

bash

#### Установите зависимости

pip install pyserial pynmea2

#### Запустите GPS монитор
python gps_monitor.py /dev/cu.usbserial-1420

#### Анализируйте логи

python gps_analyzer.py gps_logs/your_log_file.txt

🛠️ Аппаратная настройка

Необходимые компоненты

Модуль ATGM336H

USB-UART преобразователь (CP2102, CH340, FT232 и т.д.)

GPS антенна

Соединительные провода

Схема подключения

text

ATGM336H        USB-UART

VCC      →      3.3V/5V

GND      →      GND

TX       →      RX

RX       →      TX

PPS      →      (Опционально) GPIO для аппаратного PPS

📁 Структура проекта

text

gps-tracker-atgm336h/

├── index.html              # Основное веб-приложение

├── gps_monitor.py          # Python инструмент мониторинга

├── gps_analyzer.py         # Инструмент анализа логов

├── config.py              # Файл конфигурации

├── requirements.txt       # Python зависимости

└── gps_logs/             # Директория логов (создается автоматически)

    ├── gps_trec_log_*.txt
    
    └── gps_data_*.txt

gps-tracker-atgm336h/
├── 📄 README.md              # Документация (этот файл)
├── 🌐 index.html             # Основное веб-приложение
├── 🐍 gps_monitor.py         # Python монитор с буферизацией
├── 📊 gps_analyzer.py        # Анализатор логов
├── ⚙️ config.py              # Конфигурационные параметры
├── 📦 requirements.txt       # Python зависимости
├── 📄 LICENSE               # MIT лицензия
└── 📁 gps_logs/             # Директория логов (создается автоматически)
    ├── gps_trec_log_*.txt
    └── gps_data_*.txt

⚙️ Конфигурация

Настройки веб-приложения

Скорость порта: 4800-115200 (по умолчанию: 9600)

Размер буфера: 1KB-16KB (по умолчанию: 4KB)

Строк в логе: 10-1000 (по умолчанию: 200)

Режим отображения: Горизонтальный/Вертикальный

Поддерживаемые NMEA сообщения

$GNGGA, $GPGGA - данные GPS фиксации

$GNRMC, $GPRMC - минимальные рекомендуемые данные

$GNGSA, $GPGSA - DOP и активные спутники

$GPGSV, $BDGSV - информация о спутниках

$GPTXT - текстовые сообщения

🎯 Примеры использования

Отслеживание в реальном времени

Подключите GPS модуль к компьютеру

Откройте веб-приложение

Нажмите "Подключиться" и выберите последовательный порт

Наблюдайте вашу позицию на карте

Мониторьте статистику спутников и качество сигнала

Анализ данных

Запишите сессию используя веб-приложение или Python скрипт

Используйте анализатор для оценки стабильности позиционирования:

bash

python gps_analyzer.py gps_logs/gps_data_20251103_182821.txt

Генерируйте отчеты о стабильности и оценках точности

🌟 Расширенные возможности

Оценка качества сигнала

Круги точности на карте на основе HDOP

Количество спутников с визуальным прогресс-баром

Классификация качества фиксации (Нет, 2D, 3D, DGPS и т.д.)

Мониторинг PPS синхронизации

Управление данными

Автоматическая ротация логов

Настраиваемые размеры буфера

Обработка обрезанных сообщений

Функциональность экспорта с метаданными

Кросс-платформенная совместимость

Веб: Chrome 89+, Edge 89+

Python: 3.7+ с pyserial

ОС: Windows, macOS, Linux

🐛 Решение проблем

Частые проблемы

Web Serial не доступен

Используйте Chrome/Edge 89+

Включите #enable-experimental-web-platform-features в chrome://flags

Убедитесь что используете HTTPS или localhost

Нет данных от GPS

Проверьте подключение (TX→RX, RX→TX)

Проверьте скорость порта (обычно 9600)

Убедитесь что антенна имеет обзор неба

Проверьте питание модуля (3.3V/5V)

Обрезанные сообщения в логах

Увеличьте размер буфера в настройках

Проверьте совместимость скорости порта

Убедитесь в стабильности USB подключения

🤝 Участие в разработке

Мы приветствуем участие! Вы можете:

Сообщать об ошибках и проблемах

Предлагать новые функции

Создавать pull requests

Улучшать документацию

📄 Лицензия

Этот проект лицензирован под MIT License - подробности в файле LICENSE.

🙏 Благодарности

Leaflet за отличную библиотеку карт

OpenStreetMap за бесплатные тайлы карт

Производителям ATGM336H за надежное GPS оборудование

Команде Web Serial API за браузерную serial коммуникацию

📞 Контакты и поддержка

Если у вас есть вопросы или предложения, создавайте issue в репозитории или свяжитесь с нами!

Happy GPS Tracking! 🛰️✨
