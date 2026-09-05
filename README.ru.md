🌍 [English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

# photoshop-helper-2026

## Улучшение рабочего процесса на Python для Adobe Photoshop

`photoshop-helper-2026` — это надежная утилита на Python, разработанная для оптимизации общих задач и автоматизации повторяющихся процессов для пользователей Adobe Photoshop. Предоставляя набор скриптов и инструментов, этот проект призван значительно повысить вашу производительность, сократить ручной труд и обеспечить согласованность в ваших рабочих процессах дизайна и обработки изображений.

Независимо от того, являетесь ли вы графическим дизайнером, фотографом или цифровым художником, `photoshop-helper-2026` предлагает интеллектуальные решения для управления вашими активами, предварительной обработки изображений и подготовки ваших проектов с большей эффективностью.

## Особенности

-   **Пакетная обработка изображений:** Автоматизируйте такие задачи, как изменение размера, добавление водяных знаков, преобразование форматов и применение базовых фильтров к нескольким изображениям.
-   **Организация активов:** Инструменты для интеллектуальной сортировки, переименования и структурирования файлов изображений и активов проекта, подготавливая их для Photoshop.
-   **Управление метаданными:** Чтение и запись метаданных изображений (EXIF, IPTC) для помощи в каталогизации и поиске.
-   **Генерация слоев (Будущее):** Скрипты для помощи в генерации шаблонных слоев или активов на основе входных данных (например, создание нескольких текстовых слоев из списка).
-   **Интеллектуальная подготовка к экспорту:** Подготовка изображений для конкретных требований экспорта (например, веб-оптимизация, форматы для печати) перед открытием их в Photoshop.
-   **Пользовательские хуки для скриптов:** Легко расширяйте функциональность помощника с помощью собственных скриптов Python, чтобы адаптировать его к уникальным рабочим процессам.

## Установка

Чтобы начать работу с `photoshop-helper-2026`, выполните следующие шаги:

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/your-username/photoshop-helper-2026.git
    cd photoshop-helper-2026
    ```

2.  **Создайте и активируйте виртуальное окружение (рекомендуется):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Установите необходимые зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

## Пример использования

Вот простой пример, демонстрирующий, как использовать `photoshop-helper-2026` для пакетного изменения размера всех изображений `.jpg` в директории `source_images` и сохранения их в директорию `output_images`.

```python
import os
from photoshop_helper.image_processor import resize_images

# Define input and output directories
input_dir = "source_images"
output_dir = "output_images"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define target dimensions (e.g., 800 pixels wide, maintaining aspect ratio)
target_width = 800

print(f"Resizing images from '{input_dir}' to '{output_dir}' with width {target_width}px...")

# Use the resize_images function
# This function would iterate through the input_dir, resize JPEGs, and save them.
# The actual implementation of resize_images would be within the photoshop_helper package.
resize_images(input_folder=input_dir, output_folder=output_dir, target_width=target_width, format="JPEG", quality=85)

print("Image resizing complete!")
print(f"Check the resized images in the '{output_dir}' directory.")
```

Чтобы запустить этот пример, сохраните его как файл Python (например, `resize_script.py`) в корневой директории вашего `photoshop-helper-2026`, убедитесь, что у вас есть папка `source_images` с несколькими файлами `.jpg`, а затем выполните:

```bash
python resize_script.py
```

## Конфигурация

`photoshop-helper-2026` можно настроить с помощью файла `config.ini`, расположенного в корневой директории проекта, или через переменные окружения для конфиденциальных настроек.