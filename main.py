def calculator(a, b, o):
    if o == 1:
        return a + b, f"{a} + {b} = {a + b}"
    elif o == 2:
        return a - b, f"{a} - {b} = {a - b}"
    elif o == 3:
        return a * b, f"{a} * {b} = {a * b}"
    elif o == 4:
        if b != 0:
            return a / b, f"{a} / {b} = {a / b}"
        else:
            return None, "Ошибка: деление на ноль!"
    elif o == 5:
        return a ** b, f"{a} ^ {b} = {a ** b}"
    elif o == 6:
        if b != 0:
            return a ** (1 / b), f"{a} ^ (1/{b}) = {a ** (1 / b)}"
        else:
            return None, "Ошибка: нельзя извлечь корень с нулевой степенью!"
    else:
        return None, "Неизвестная операция!"

help_text = (
    "Доступные функции:\n"
    "1) Сложение\n"
    "2) Вычитание\n"
    "3) Произведение\n"
    "4) Деление\n"
    "5) Возведение в степень\n"
    "6) Корень из числа\n"
    "history - показать историю\n"
    "help - справка\n"
    "0 - выход\n"
)

print("Добро пожаловать в калькулятор!")
print(help_text)

history = []
result = None  # для многоразовых вычислений

while True:
    try:
        o = input("Выберите функцию (1-6), history, help или 0 для выхода: ").strip()
        if o == "0":
            print("Выход. До свидания!")
            break
        if o.lower() == "help":
            print(help_text)
            continue
        if o.lower() == "history":
            if history:
                print("История вычислений:")
                for h in history:
                    print(h)
            else:
                print("История пуста.")
            continue
        if o.isdigit():
            o = int(o)
            if o not in range(1, 7):
                print("Некорректная функция!")
                continue
            # Многоразовые вычисления
            use_last = False
            if result is not None:
                use_last = input("Использовать результат предыдущего вычисления как первое число? (y/n): ").strip().lower() == "y"
            if use_last and result is not None:
                a = result
            else:
                a = float(input("Введите 1 число: "))
            b = float(input("Введите 2 число: "))
            result, hist = calculator(a, b, o)
            print(hist)
            history.append(hist)
        else:
            print("Введите номер функции, help, history или 0 для выхода.")
    except ValueError:
        print("Ошибка: введите корректное число!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except KeyboardInterrupt:
        print("\nВыход по Ctrl+C")
        break
