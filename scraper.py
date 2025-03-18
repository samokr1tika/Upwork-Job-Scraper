import requests
import json
import logging
from config import API_KEY, SEARCH_QUERY, MIN_BUDGET, SAVE_TO, LANGUAGE

# Перевод сообщений
messages = {
    "ru": {
        "start": "Начинаю поиск заказов...",
        "no_jobs": "Ничего не найдено.",
        "saved": "Сохранено {count} вакансий в {file}",
        "request_error": "Ошибка запроса: {error}"
    },
    "en": {
        "start": "Starting job search...",
        "no_jobs": "No jobs found.",
        "saved": "Saved {count} jobs to {file}",
        "request_error": "Request error: {error}"
    }
}

# Выбор языка
msg = messages.get(LANGUAGE, messages["en"])

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

UPWORK_API_URL = "https://www.upwork.com/api/jobs"

def get_jobs():
    """Запрос вакансий с Upwork API."""
    params = {
        "q": SEARCH_QUERY,
        "min_budget": MIN_BUDGET,
        "limit": 10
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(UPWORK_API_URL, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("jobs", [])
    except requests.exceptions.RequestException as e:
        logging.error(msg["request_error"].format(error=e))
        return []

def save_jobs(jobs):
    """Сохранение вакансий в файл."""
    with open(SAVE_TO, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
    logging.info(msg["saved"].format(count=len(jobs), file=SAVE_TO))

def main():
    logging.info(msg["start"])
    jobs = get_jobs()
    if jobs:
        save_jobs(jobs)
    else:
        logging.info(msg["no_jobs"])

if __name__ == "__main__":
    main()
