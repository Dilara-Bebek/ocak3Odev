

# 1’den 100’e kadar olan sayıları ekrana yazdırma
print("1'den 100'e kadar olan sayılar:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")


# 1’den 100’e kadar sadece çift sayıları yazdırma
print("1'den 100'e kadar olan çift sayılar:")
for i in range(2, 101, 2):
    print(i, end=" ")
print("\n")



# Kullanıcının girdiği sayının faktöriyelini hesaplama
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")



# 1’den 100’e kadar olan tüm asal sayıları bulma
print("1'den 100'e kadar olan asal sayılar:")
for numara in range(2, 101): #en küçük asal sayı 2,2 den başlarız
    asal = True
    for i in range(2, int(numara ** 0.5) + 1):  #kareköküne kadar olan kısmı kontrol ederiz
        if numara % i == 0:
            asal = False
            break
    if asal:
        print(numara, end=" ")


