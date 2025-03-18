# Upwork Job Scraper (RU/EN)

## 🇷🇺 Описание  
Этот скрипт ищет заказы на Upwork по заданным параметрам и сохраняет их в файл.  

## 🇬🇧 Description  
This script searches for jobs on Upwork based on given parameters and saves them to a file.  

### 🔧 Установка / Installation  

1. **Установи зависимости** / **Install dependencies**  
   ```bash
   pip install requests
   ```

2. **Настрой конфиг (`config.py`)** / **Configure `config.py`**  
   - `API_KEY` – Upwork API ключ / API Key  
   - `SEARCH_QUERY` – Запрос / Search Query  
   - `MIN_BUDGET` – Минимальный бюджет / Minimum Budget  
   - `SAVE_TO` – Файл сохранения / Output File  
   - `LANGUAGE` – Язык (`ru` / `en`) / Language (`ru` / `en`)  

3. **Запусти скрипт** / **Run the script**  
   ```bash
   python scraper.py
   ```

### 📁 Вывод / Output  
Результаты сохраняются в `results.json`.  
Results are saved in `results.json`.  
