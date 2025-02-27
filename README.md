```md
# 📊 Order Book Analyzer

> **FastAPI-сервіс для збору та аналізу ордербуку**  
> Виявляє аномалії в ринкових заявках (сплески, відхилення, аномальні об'єми).

---

## 📌 Особливості

✅ **Збір даних** — отримує інформацію про ордербук з API  
✅ **Аналіз аномалій** — виявляє підозрілі зміни в об'ємах і цінах  
✅ **Гнучкість** — використовує **FastAPI** для швидкої роботи  
✅ **Зручність** — легко розгортається на **Heroku**  

---

## 🚀 Швидкий старт

### 1️⃣ Встановлення залежностей
```bash
# Клонування репозиторію
git clone https://github.com/your_repo/orderbook_analyzer.git
cd orderbook_analyzer

# Створення та активація віртуального середовища
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

# Встановлення залежностей
pip install -r requirements.txt
```

### 2️⃣ Запуск локально
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
> **Після запуску API буде доступне за адресою:**  
> 👉 `http://127.0.0.1:8000/docs` (Swagger UI)  

---

## 🛠 API Ендпоінти

| Метод | URL           | Опис |
|--------|--------------|----------------------------------------|
| `GET`  | `/`          | Перевіряє, чи API працює |
| `GET`  | `/fetch`     | Отримує дані ордербуку з API |
| `POST` | `/analyze`   | Аналізує ордербук та повертає аномалії |

### 📌 Запит на аналіз:
```bash
curl -X POST "http://127.0.0.1:8000/analyze" -H "Content-Type: application/json" -d '{"bids": [[0.1809, 281247.50], [0.1805, 11.28]], "asks": [[0.1804, 97907.65], [0.1796, 8.62]]}'
```
#### ✅ Приклад відповіді:
```json
{
  "volume_anomalies": [...],
  "price_anomalies": [...],
  "local_spikes": [...],
  "boundary_anomalies": [...]
}
```

---

## ✅ Запуск тестів

```bash
pytest tests/
```

---

## 🌐 Деплой на Heroku

### 1️⃣ Встановлення Heroku CLI (якщо ще немає)
[Завантажити тут](https://devcenter.heroku.com/articles/heroku-cli)

### 2️⃣ Логін у Heroku
```bash
heroku login
```

### 3️⃣ Створення додатку
```bash
heroku create my-fastapi-app
```

### 4️⃣ Додавання віддаленого репозиторію та деплой
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### 5️⃣ Відкриття додатку
```bash
heroku open
```

---

## 🔗 Файлова структура

```
📂 project_root/
│── 📂 app/               # Основний код
│   │── __init__.py
│   │── main.py           # FastAPI додаток
│   │── data.py           # Завантаження ордербуку
│   │── utils.py          # Функції аналізу
│   │── analysis.py       # Аналіз аномалій
│── 📂 tests/             # Юніт-тести
│   │── test_data.py
│   │── test_utils.py
│   │── test_analysis.py
│── requirements.txt      # Список залежностей
│── Procfile              # Налаштування для Heroku
│── runtime.txt           # Вказує Python-версію
│── README.md             # Документація
```

---

## 🏗 Використані технології

🔹 **Python** — основна мова  
🔹 **FastAPI** — швидкий API-фреймворк  
🔹 **Pandas** — обробка фінансових даних  
🔹 **Requests** — отримання інформації з API  
🔹 **Uvicorn** — запуск ASGI-сервера  
🔹 **Heroku** — хостинг для деплою  

---

## 🛠 Подальші покращення

- [ ] Додати кешування для API-викликів  
- [ ] Інтеграція з реальними біржами
- [ ] Збереження аналізу у базу даних  

---
