def ceaser_cip(word):
    # q1 = input('Какое направление: шифрование или дешифрование? 0 или 1 \n')
    q1 = '0'
    # q2 = input('Язык алфавита? ru или en? \n')
    q2 = 'en'
    # q3 = int(input('шаг сдвига? \n'))
    count = 0
    for i in word:
        if i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
            count += 1
    q3 = count

    text = 'Умом Россию не понять'
    text = 'Блажен, кто верует, тепло ему на свете!0'
    text = 'To be, or not to be, that is the question!'
    text = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
    text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
    text = 'Hawnj pk swhg xabkna ukq nqj.'
    text = word
    new_text = ''

    if q1 == '0':
        q_arr = 1
    else:
        q_arr = -1

    if q2 == 'ru':
        q_abc = 32
        q_a_min = ord('а')
        q_a_max = ord('я')
        q_b_min = ord('А')
        q_b_max = ord('Я')
    else:
        q_abc = 26
        q_a_min = ord('a')
        q_a_max = ord('z')
        q_b_min = ord('A')
        q_b_max = ord('Z')

    for i in range(len(text)):
        if q_a_min <= ord(text[i]) <= q_a_max:
            if q_a_min <= ord(text[i]) + q_arr * q3 <= q_a_max:
                new_text += chr(ord(text[i]) + q_arr * q3)
            else:
                new_text += chr(ord(text[i]) + q_arr * q3 - q_abc * q_arr)
        elif q_b_min <= ord(text[i]) <= q_b_max:
            if q_b_min <= ord(text[i]) + q_arr * q3 <= q_b_max:
                new_text += chr(ord(text[i]) + q_arr * q3)
            else:
                new_text += chr(ord(text[i]) + q_arr * q3 - q_abc * q_arr)
        else:
            new_text += text[i]

    return new_text

n = [ceaser_cip(i) for i in input().split()]
print(*n)

