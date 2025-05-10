#Not ekleme fonskiyonu
def not_ekle():
    not_metni = input("Eklemek İstediginiz Notu Yaziniz:")
    #with open ile birlikte notlar.txt adında yeni bir dosya oluştur varsa da sonuna ekle
    with open("notlar.txt", "a", encoding="utf-8") as dosya: # utf-8 türkçe karakterin bozulmamasi için gerekli
        dosya.write(not_metni + "/n") # "a" sağlar -> dosya'nın sonuna da ekle ve bir satır aşağı çek
    print("Not Başariyla Kaydedildi")

#Not göster fonksiyonunu oluşturalım
def notlari_goster():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya: # "r" dosya okuma modudur
            notlar = dosya.readlines() #dosyadaki tüm satırları oku ve notlar içerisine yaz
            if notlar: #not listesi boş değilse çalışır
                print("\n--- Kayededilen Notlar---")
                for i, notSatiri in enumerate(notlar,start=1): #her not için hem sırayı hem de içeriği ekrana bastırır
                    print(f"{i}.{notSatiri.strip()}") #satır sonundaki /n siler
                    print()#boşluk bırakmak için kullanılabilir
            else: #notlar listesi boşsa da:
                print("Henüz not bulunamiyor...\n")
    except FileNotFoundError:
        print("Henüz hiç not eklenmemiş.")

#Notları Temizle Fonskiyonu
def notlari_temizle():
    with open("notlar.txt", "w",encoding="utf-8"): #dosyayı temizleyip sıfırdan olusturur
        pass #burada hiçbir şey yapma anlamındadir(sadece temizleme amaçlı)
    print("Tüm Dosyalar Silindi")

#Main Fonskiyonu
def main():
    while True:
        print("===Not Defteri Uygulamasina Hosgeldiniz===")
        print("1. Yeni Not Ekle")
        print("2. Notlari Goster")
        print("3. Tüm Notlari Sil")
        print("4. Çikis")
        secim = input("Seciminizi Yapin(1-4): ")

        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_goster()
        elif secim == "3":
            notlari_temizle()
        elif secim == "4":
            print("Uygulma Kapaniyor...")
            break
        else:
            print("Geçersiz Seçim. Lütfen 1-4 arasi bir deger giriniz! ")

if __name__ == "__main__":
    main()

