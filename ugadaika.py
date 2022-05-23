import random

def is_valid(st):
    if st.isdigit() and 1 <= int(st) <= 100:
        return True
    else:
        return False

n = random.randint(1, 100)
print('Угадайка число от 1 до 100 включительно!')
flag = True
count = 0
while flag:
    number = input('Введите число \n')
    if not is_valid(number):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        number = int(number)
        count += 1
        if number < n:
            print('Слишком мало, попробуйте еще раз! Количество попыток =', count)
        elif number > n:
            print('Слишком много, попробуйте еще раз! Количество попыток =', count)
        else:
            print('Вы угадали, поздравляем! Количество попыток =', count)
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')