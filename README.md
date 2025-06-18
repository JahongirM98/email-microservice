# Email Microservice

Микросервис на FastAPI для отправки и получения электронной почты через SMTP и IMAP.

---

## 📦 Возможности

- 📤 Отправка писем через SMTP (`POST /emails/send`)
- 📥 Получение входящих писем через IMAP (`GET /emails`)
- 📊 Получение статистики писем за период (`GET /emails/stats`)
- 🔍 Фильтрация писем по дате, теме и email
- 🧪 Покрытие базовыми тестами (pytest)
- 🐳 Запуск через Docker и Docker Compose
- 📚 Swagger UI по адресу `/docs`

---

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-username/email-microservice.git
cd email-microservice
```

### 2. Настройте переменные окружения

Создайте файл `.env`:

```env
# SMTP (Mailpit)
SMTP_HOST=mailpit
SMTP_PORT=1025

# IMAP (например, Gmail)
IMAP_HOST=imap.gmail.com
IMAP_PORT=993
IMAP_USER=your_email@gmail.com
IMAP_PASS=your_app_password
```

> ⚠️ Для Gmail требуется включить двухфакторную аутентификацию и создать пароль приложения:  
> https://myaccount.google.com/apppasswords

---

### 3. Запуск сервиса

```bash
docker compose up --build
```

Открой Swagger-документацию:  
👉 http://localhost:8000/docs

---

### 4. Примеры

#### 📤 Отправка письма

`POST /emails/send`

```json
{
  "to": ["test@example.com"],
  "subject": "Привет",
  "body": "Это тело письма",
  "is_html": false
}
```

#### 📥 Получение входящих писем

`GET /emails?limit=10&subject=invoice&email=gmail.com`

#### 📊 Получение статистики

`GET /emails/stats?from_date=2024-01-01&to_date=2025-01-01`

---

### 🧪 Тестирование

```bash
docker compose run --rm app pytest
```

---

## 🗂 Структура

```
email-microservice/
├── app/
│   ├── api/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
│   └── test_emails.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## 🔗 Автор

Разработано в рамках тестового задания на позицию Python-разработчика.