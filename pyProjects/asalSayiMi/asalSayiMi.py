def asalSayiMi(sayi):
    if sayi <2:
        print("Sayiniz Asal Degildir")
        return # return burada her şeyi bırakıp programı sonlandırır
    flag = 0

    for i in range(2, sayi//2):
        if sayi % i == 0:
            flag =1
            break #bolen bulunduysa devam etmeye gerek yok

    if flag == 0:
        print("Sayiniz Asaldir")
    else:
        print("Sayiniz Asal Degildir")

def main():
    sayi1 = int(input("Lutfen bir sayi Giriniz"))
    asalSayiMi(sayi1)

if __name__ == "__main__":
    main()

    
