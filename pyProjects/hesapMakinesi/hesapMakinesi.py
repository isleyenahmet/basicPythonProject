#Hesapla Fonksiyonu
def hesapla(sayi1,sayi2,islem):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            return "Hata: Sifira Bölme Hatasi"
        return sayi1 / sayi2
    else:
        return "Hata: Gecersiz İşlem"
    
#Main fonksiyonu
def main():
    print("===Hesap Makinesi===")
    try:
        sayi1 = float(input("Birinci Sayiyi Giriniz:"))
        islem = input("İslem Giriniz:")
        sayi2 = float(input("İkinci Sayiyi Giriniz:"))
        sonuc = hesapla(sayi1,sayi2,islem)
        print(f"Sonuc: {sonuc}")
    except ValueError:
        print("Hata: Lutfen Gecerli Bir Sayi Giriniz: ")

#C++ veya benzeri dillerdeki gibi direkt main okumaz. senin maini ilk okumasi için alttaki satirlari yazman gerekir
if __name__ == "__main__":
    main()

