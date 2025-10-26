import random
import time

def summon_potion():
    ingredients = ["крыло летучей мыши", "слеза феникса", "пыльца единорога"]
    print("🧪 Варю зелье...")
    time.sleep(1.5)
    print(f"Добавляю {random.choice(ingredients)}...")
    time.sleep(1)
    print("💥 Зелье готово! Оно светится!")

summon_potion()