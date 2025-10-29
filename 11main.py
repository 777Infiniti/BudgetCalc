def check_number(num):
    # Проверяем, является ли число целым
    if isinstance(num, int):
        # Проверяем четность
        if num % 2 == 0:
            return f"{num} - целое и четное число"
        else:
            return f"{num} - целое и нечетное число"
    else:
        return f"{num} - не целое число"

