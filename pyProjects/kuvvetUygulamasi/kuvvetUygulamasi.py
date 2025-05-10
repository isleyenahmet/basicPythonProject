def kuvvetUygulamasi(sayi,kuvvet):
    carpim=1
    for i in range(1,kuvvet+1):
        carpim = carpim * sayi
    print(f"Sonuc: {carpim}")

def main():
    sayi = int(input("Kuvvetini Almak istediginiz Sayiyi Giriniz:"))
    kuvvet = int(input("Kaçinci Dereceden kuvvet almak istiyosunuz"))
    kuvvetUygulamasi(sayi,kuvvet)


if __name__ == "__main__":
    main()
