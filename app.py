from flask import Flask, request, render_template_string
from logic import calculate_sum

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>Arithmetic Progression Sum ${\n}by Laptev Oleksandr</title></head>
<body>
    <h2>Обчислення суми арифметичної прогресії (2, 4, 6...)</h2>
    <form method="post">
        Введіть кількість членів (n): <input type="number" name="n_value" required>
        <input type="submit" value="Обчислити">
    </form>
    {% if result is not none %}
        <h3>Результат для n={{ n }}: {{ result }}</h3>
    {% endif %}
    {% if error %}
        <h3 style="color:red">Помилка: {{ error }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    n = None
    error = None
    if request.method == "POST":
        try:
            n_input = request.form.get("n_value")
            n = int(n_input)
            result = calculate_sum(n)
        except (ValueError, TypeError):
            error = "Будь ласка, введіть коректне ціле число."
            
    return render_template_string(HTML_TEMPLATE, result=result, n=n, error=error)

if __name__ == "__main__":
    # Слухаємо на всіх інтерфейсах для роботи в Docker
    app.run(host='0.0.0.0', port=5000)