import random

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(list(chars))
    return password


digits = '0123456789'
lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
punctuation = '!#$%&+=-*?@^_'
bad_letters = 'il1Lo0O'

chars = ''

count = int(input('Какое количество паролей для генерации надо сделать?'))
pass_len = int(input('Длина одного пароля'))
q1 = int(input('Включать ли цифры? 1 - да, 0 - нет'))
q2 = int(input('Включать ли прописные буквы? 1 - да, 0 - нет'))
q3 = int(input('Включать ли строчный буквы? 1 - да, 0 - нет'))
q4 = int(input('Включать ли символы? 1 - да, 0 - нет'))
q5 = int(input('Исключать ли неоднозначные символы? il1Lo0O  1 - да, 0 - нет'))
chars += digits * q1 + lowercase_letters * q2 + uppercase_letters * q3 + punctuation * q4
for i in bad_letters:
    chars = chars.replace(i,'')

for _ in range(count):
    print(generate_password(pass_len, chars))