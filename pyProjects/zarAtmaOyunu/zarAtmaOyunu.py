#Zar Atma Oyunu
import random

def zar_at():
    return random.randint(1,6)

def oyuncu_oyna(oyuncu_adi):
    toplam = 0
    print(f"{oyuncu_adi} zar atiyor: ")
    for i in range(1,4):
        zar = zar_at()
        toplam += zar
        print(f"{i}. zar: {zar}")
    print(f"{oyuncu_adi} toplam puani: {toplam}\n")
    return toplam

def main():
    oyuncu1_adi = input("1. Oyuncunun Adini Giriniz: ")
    oyuncu2_adi = input("2. Oyuncunun Adini Giriniz: ")

    puan1 = oyuncu_oyna(oyuncu1_adi)
    puan2 = oyuncu_oyna(oyuncu2_adi)

    if puan1 > puan2:
        print(f"{oyuncu1_adi} Kazandi!")
    elif puan2 > puan1:
        print(f"{oyuncu2_adi} Kazandi!")
    else: print("Puanlar Eşit Dostluk Kazandi")


if __name__ == "__main__":
    main()
