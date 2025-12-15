# cli.py
import sys
from logic import calculate_sum

def run_console_app():
    print("==========================================")
    print(" ОБЧИСЛЕННЯ СУМИ ПРОГРЕСІЇ (2, 4, 6...)")
    print(" Введіть 'q' або 'exit' щоб вийти.")
    print("==========================================")

    while True:
        try:
            user_input = input("\nВведіть кількість членів (n): ").strip()

            # Перевірка на вихід
            if user_input.lower() in ['q', 'exit']:
                print("Програма завершена. До побачення!")
                break

            # Конвертація та обчислення
            n = int(user_input)
            result = calculate_sum(n)
            
            print(f"-> Сума перших {n} членів дорівнює: {result}")

        except ValueError:
            # Це спрацює, якщо int() не зможе перетворити рядок (наприклад, введені літери)
            # Або якщо calculate_sum викине ValueError (для від'ємних чисел)
            print("ПОМИЛКА: Будь ласка, введіть коректне ціле невід'ємне число.")
        except Exception as e:
            print(f"Непередбачена помилка: {e}")

if __name__ == "__main__":
    run_console_app()