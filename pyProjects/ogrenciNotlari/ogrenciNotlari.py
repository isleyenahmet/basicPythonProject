def not_ortalamasi(notlar):
    #Notlarin ortalamasini Hesaplayacağizz
    toplam = sum(notlar) # notlarin toplamini al
    ortalama = toplam / len(notlar) #toplami not sayisina(ogrenci) sayisina boler
    return ortalama #ortalama degerini dondur

def max_min_not(notlar):
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)
    return en_yuksek, en_dusuk #max mini geri doner

def gecerli_notlar(notlar):
    return len([not_ for not_ in notlar if not_ >=60]) #60 ve üzeri notlari al

def main():
    notlar = [] # notlar adında bir dizi oluşturuyorum

    num_of_students = int(input("Kaç Öğrencinin Notunu Gireceksiniz?"))
    for i in range(num_of_students):
        not_ = float(input(f"{i+1}. öğrencinin Notunu Giriniz: "))
        notlar.append(not_) #alınan notu listeye ekliyoruz

    #notlar üzerinden işlem yapalım
    ortalama = not_ortalamasi(notlar)
    en_yuksek, en_dusuk = max_min_not(notlar)
    gecerli_notlarin_adedi = gecerli_notlar(notlar)

    print(f"\nÖğrencilerin Notlari: {notlar}")
    print(f"Notlarin Ortalamasi: {ortalama}")
    print(f"En Yüksek Not: {en_yuksek}")
    print(f"En Düşük Not: {en_dusuk}")
    print(f"Geçerli Notlar(60 ve üzeri notlar): {gecerli_notlarin_adedi} ögrenci")


if __name__ == "__main__":
    main()