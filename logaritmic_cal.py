import math

def log_calculator():
    print("Логарифмический калькулятор")
    print("1. Натуральный логарифм (ln)")
    print("2. Десятичный логарифм (log10)")
    print("3. Логарифм по произвольному основанию")
    
    choice = input("Выберите тип логарифма (1-3): ")
    
    try:
        # Ввод числа для вычисления логарифма
        x = float(input("Введите число (x > 0): "))
        
        if x <= 0:
            print("Ошибка: Число должно быть положительным!")
            return
            
        if choice == "1":
            result = math.log(x)
            print(f"ln({x}) = {result:.6f}")
            
        elif choice == "2":
            result = math.log10(x)
            print(f"log10({x}) = {result:.6f}")
            
        elif choice == "3":
            base = float(input("Введите основание логарифма (a > 0, a ≠ 1): "))
            if base <= 0 or base == 1:
                print("Ошибка: Основание должно быть положительным и не равным 1!")
                return
            result = math.log(x, base)
            print(f"log_{base}({x}) = {result:.6f}")
            
        else:
            print("Ошибка: Неверный выбор!")
            
    except ValueError:
        print("Ошибка: Введите корректное число!")

# Запуск калькулятора
if __name__ == "__main__":
    log_calculator()