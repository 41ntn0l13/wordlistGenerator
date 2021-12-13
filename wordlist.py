import itertools
import re

print("""

Yontem secin: 

1) Uzunluk ve belirlenin sayiya gore olustur
2) Belirlenen cumledeki kelimelerle olustur

""")
yontem = int(input("> "))

if yontem == 1:
    harf = input("hangi harfler olsun: ")
    uzunluk = int(input("uzunlugu belirtin: "))
    for ded in itertools.product(harf, repeat=uzunluk):
        m = ''.join(ded)
        f = open("wordlist.txt", "w")
        f.write(m+"\n")
        f.close

elif yontem == 2:
    cumle = input("Cumlenizi girin: ")
    splitmetod = re.split(r"[-;,.'\s]\s*",cumle)
    dedz = open("wordlist2.txt","w")
    for qwerty in splitmetod:
        print(qwerty)
        dedz.write(qwerty+"\n")
    dedz.close()
     
