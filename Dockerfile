# Використовуємо легкий образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл залежностей та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проекту в контейнер
COPY . .

# Відкриваємо порт 5000
EXPOSE 5000

# Команда запуску
CMD ["python", "app.py"]