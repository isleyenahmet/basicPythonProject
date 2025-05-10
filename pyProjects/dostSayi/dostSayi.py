def dostSayiMi(sayi1,sayi2):

    toplamSayi1 = 0
    toplamSayi2 = 0

    for i in range(1,sayi1):
        if sayi1 % i == 0:
            toplamSayi1 += i

    for i in range(1,sayi2):
        if sayi2 % i == 0:
            toplamSayi2 += i

    if toplamSayi1 == sayi2 and toplamSayi2 == sayi1:
        print("Dost Sayidir")
    else:
        print("Dost Sayi Degildir")

def main():
    sayi1 = int(input("1.Sayiyi Giriniz: "))
    sayi2 = int(input("2.Sayiyi Giriniz: "))
    dostSayiMi(sayi1,sayi2)

if __name__ == "__main__":
    main()
    