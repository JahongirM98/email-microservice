FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /code

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY ./app ./app
COPY ./tests ./tests

# Устанавливаем переменную окружения для импорта app.*
ENV PYTHONPATH=/code

# Запуск Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
