#Cначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

iht_n = int(input('Введите число "N": '))
print('Введите ровно "N" целых чисел: ')
count = 0
for i in range(iht_n):
    n = int(input())
    if n == 0:
        count += 1
    else:
        count += 0
print(f'Из них = 0: {count}')                
