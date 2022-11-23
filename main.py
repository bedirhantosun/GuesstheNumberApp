from random import randint

rand = randint(1,100)
counter = 0

while True:
    counter += 1
    number = int(input('1 ile 100 arasında bir değer giriniz (0 Çıkış):'))
    if number == 0:
        print('Oyunu iptal ettiniz')
        break
    elif number < rand:
        print('Daha Yüksek Bir sayi giriniz:')
        continue
    elif number > rand:
        print('Daha düşük bir sayi giriniz:')
        continue
    else:
        print('Rastgele secilen sayi {0}!'.format(rand))
        print('Tahmin sayiniz {0}'.format(counter))