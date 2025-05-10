#Banka Uygulamasi
para = 1000 #Parayı Global Tanımladık

def para_cek(cekilecekMiktar):
    global para
    if cekilecekMiktar > para:
        print("Yetersiz Bakiye")
    else:
        para = para - cekilecekMiktar
    return para

def para_yatir(yatirilacakMiktar):
    global para
    para = para + yatirilacakMiktar
    return para

def bakiye_gor():
    global para
    print(para)
    return para

def main():
    global para
    while True:
    
        print("---Banka Uygulamasina Hos Geldiniz---\n")
        #Banka İşlemleri
        print("1.Para Cekmek")
        print("2.Para Yatirmak")
        print("3.Tüm Bakiyeyi Görmek")
        print("4.Cikis Yapmak")
        secenek = int(input("Hangi İşlemi Gerçekleştireceksiniz: "))

        if secenek == 1:
            cekilecekMiktar = int(input("Cekilmek istenen miktari Giriniz: "))
            para_cek(cekilecekMiktar)
        elif secenek == 2:
            yatirilacakMiktar = int(input("Yatirilacak Miktari Giriniz: "))
            para_yatir(yatirilacakMiktar)
        elif secenek == 3:
            bakiye_gor()
        elif secenek == 4:
            print("Uygulama Kapaniyor...")
            break
        else: print("Gecersiz bir secenek Lutfen 1-4 arasinda bir deger giriniz!")

if __name__ == "__main__":
    main()