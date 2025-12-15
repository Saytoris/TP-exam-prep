FROM python:3.9-slim

WORKDIR /app

# Копіюємо файли (requirements можна залишити, навіть якщо там flask, він не заважатиме)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask порт нам для консолі не потрібен, але можна залишити
# EXPOSE 5000 

# ЗМІНИТИ: Запускаємо cli.py замість app.py
CMD ["python", "cli.py"]