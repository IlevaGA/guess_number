import random

random_num = random.randint(1, 100)
print("Угадай число от 1 до 100")

while True:
    person_num = int(input())
    if person_num < random_num:
        print("Ваше число меньше того, что загадано")
    elif person_num > random_num:
        print("Ваше число больше того, что загадано")
    elif person_num == random_num:
        print("Отличная интуиция! Вы угадали число :)")
        break
