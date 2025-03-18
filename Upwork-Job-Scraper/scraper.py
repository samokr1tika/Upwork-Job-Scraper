import requests
import json

API_URL = "https://api.upwork.com/jobs"
PARAMS = {"budget_min": 50, "budget_max": 500}

def fetch_jobs():
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()  # Вызывает ошибку, если статус ответа не 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return []

def save_jobs(jobs):
    try:
        with open("jobs.json", "w", encoding="utf-8") as file:
            json.dump(jobs, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")

if __name__ == "__main__":
    jobs = fetch_jobs()
    if jobs:
        save_jobs(jobs)
        print("Результаты сохранены в jobs.json")
    else:
        print("Нет данных для сохранения.")
