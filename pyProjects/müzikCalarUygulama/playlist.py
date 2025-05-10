import random
playlist = []

def sarki_ekle(eklenen_sarki):
    playlist.append(eklenen_sarki) #append listeye ekleme işlemi yapar
    print(f"{eklenen_sarki} listeye eklendi")

def sarki_sil(silinen_sarki):
    if silinen_sarki in playlist:
        playlist.remove(silinen_sarki)
        print(f"{silinen_sarki} listeden kaldirilidi!")
    else: print("Aranan Sarki Listede Bulunamadi")

def tum_liste_goster():
    if playlist: 
        print("Tüm Sarkilar:")
        i = 1
        for sarki in playlist: #playlisti dolaş ve bunları sarki içine at
            print(f"{i}. {sarki}")
            i +=1
    else: 
       print("Calma Listesi Boş!")

def random_sarki_cal():
    if playlist: #playlist boş değilse anlamına gelir
        sarki = random.choice(playlist)
        print(f"Şu an Calinan Şarki: {sarki}")
    else:
        print("Liste Boş. Once Listeye Sarki Ekleyin")




def main():
    while True:
        print("---Playlist Uygulamasina Hoşgeldiniz---")
        print("1. Şarki Ekle")
        print("2. Şarki Sil")
        print("3. Tüm Listeyi Goster")
        print("4. Random Şarki Cal")
        print("5. Cikis Yap")
        secenek = int(input("Bir Secenek Giriniz: "))

        if secenek == 1:
            ekelenen_sarki = input("Sarki Adini Giriniz:")
            sarki_ekle(ekelenen_sarki)
        elif secenek == 2:
            silinen_sarki = input("Sarki Adini Giriniz: ")
            sarki_sil(silinen_sarki)
        elif secenek == 3:
            tum_liste_goster()
        elif secenek == 4:
            random_sarki_cal()
        elif secenek == 5:
            print("Cikis Yapiliyor...")
            break
        else:
            print("Lutfen Gecerli Bir Deger Giriniz!")

if __name__ == "__main__":
    main()
        
    
