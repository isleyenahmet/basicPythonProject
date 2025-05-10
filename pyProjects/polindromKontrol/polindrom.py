def polindrom_kontrol_uygulamasi(metin):
    temiz_metin = ''.join(metin.lower().split()) 
    #lower ile hepsi küçük harf yapıldı.
    #slipt ile kelimelerdeki tüm harfler boşluklardan arındarak char haline getirildi
    #join ile de boşluklar dahil edilmeden char olarak ayrılan metin tekrardan string haline getirildi

    #metni tersi ile aynı mı diye kontrol edelim
    if temiz_metin == temiz_metin[::-1]: #buradaki ::-1 ifadesi degeri tersen oku anlamına gelir
        return "Polindrom"
    else: return "Polindrom Degil"

def main():
    kullaniciGirisi = input("Lutfen Bir Metin Giriniz: ")
    sonuc = polindrom_kontrol_uygulamasi(kullaniciGirisi)
    print(f"Sonuc: {sonuc}")

#main'e odaklan
if __name__ == "__main__":
    main()


