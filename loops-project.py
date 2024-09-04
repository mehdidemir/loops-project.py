"""
1-100 arasinda üretilecek bir sayiyi aşaği yukari ifadeleri ile buldurmauyaçalişin. (hak=5)
   ** "random modülü" için "python random" şeklinde arama yapin.
   ** 100 üzerinden puanlama yapin. Her soru 20 puan.
   **hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi üzerinden hesaplansin. 
"""

import random
sayi = random.randint(1, 100)
can = int(input('kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0
while hak > 0:
    hak-=1
    sayac+=1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'tebrikler {sayac}. denemede bildiniz. Toplam puaniniz: {100-(100/can)*(sayac-1)}') 
        break
    elif sayi > tahmin:
        print('yukari')
    elif sayi < tahmin:
        print('aşşaği')
    if hak == 0:
        print(f'hakkınız bitti, doğru cevap {sayi} olmalıydı')

