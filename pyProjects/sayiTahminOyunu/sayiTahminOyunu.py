#random kütüphanesini dahil etmemiz gerekiyor
import random

#sayi tahmin fonskiyonu oluştur
def sayi_tahmin_oyunu():
    print("===Sayi Tahmin Oyunu===")
    print("Hoş Geldiniz. 0-100 Arasinda bir sayi tahmin eder misiniz?")

    gizli_sayi = random.randint(0,100)
    tahmin_sayisi = 0

    while True:
    #try-excetp var yine
        try:
            tahmin = int(input("Tahmininiz: "))
            tahmin_sayisi += 1

            if tahmin > gizli_sayi:
                print("Daha Küçük Bir Sayi Giriniz: ")
            elif tahmin < gizli_sayi:
                print("Daha Büyük Bir Sayi Giriniz: ")
            else:
                print("Tebrikler Doğru Tahimin Ettiniz\n")
                print(f"Dogru Sayi: {gizli_sayi}, Tahmin Sayisi: {tahmin_sayisi} ")
                break

        except ValueError:
            print("Gecersiz Deger Girdiniz!")

#ana fonksiyonu sisteme veremem lazım 
if __name__ == "__main__":
    sayi_tahmin_oyunu()
    
        



