#fibonacci
def fibonacci_uret(adet):
    fibonacci=[0, 1] #başlangıç fibonacci sayilari

    for i in range(2,adet): #range, 2 den adete kadar git menzil anlamına gelir
        yeni_sayi = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(yeni_sayi) #fibonacci içerisine yeni sayımızı sona dahil ettik

    return fibonacci[:adet] #kullanci kac adet isterse ona göre sonuncusu da dahil olmadigi için ekrana getirir
def main():
    try:
        adet = int(input("Kaç Adet Fibonacci Sayisi İstiyorsunuz: "))
        if adet <=0:
            print("Lutfen Pozitif Bir Sayi Giriniz!")
        else:
            sonuc = fibonacci_uret(adet)
            print(f"Fibonacci Sayilariniz: {sonuc}") 
    except ValueError:
        print("Girilen Deger Gecersiz!")

# main fonc okumaik için:
if __name__ == "__main__":
    main()