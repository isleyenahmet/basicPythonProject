import random
#Film Tavisyesi Uygulamasi
aksiyon_filmleri = ["Mad Max: Fury Road", "John Wick", "Gladiator", "The Dark Knight", "Die Hard", "Inception", "The Matrix"]
macera_filmleri = ["Indiana Jones: Raiders of the Lost Ark", "The Lord of the Rings: The Fellowship of the Ring", "Jurassic Park", "Pirates of the Caribbean: The Curse of the Black Pearl", "The Revenant", "Life of Pi", "The Hobbit: An Unexpected Journey"]
komedi_filmleri = ["The Hangover", "Superbad", "Monty Python and the Holy Grail", "Step Brothers", "Dumb and Dumber", "Groundhog Day", "Bridesmaids"]
korku_filmleri = ["The Conjuring", "Hereditary", "The Exorcist", "A Nightmare on Elm Street", "Get Out", "It", "The Ring"]
gerilim_filmleri = ["Se7en", "Gone Girl", "Shutter Island", "Prisoners", "Zodiac", "The Silence of the Lambs", "Nightcrawler"]
animasyon_filmleri = ["Toy Story", "Spirited Away", "Up", "Coco", "Finding Nemo", "Inside Out", "The Lion King"]
western_filmleri = ["The Good, the Bad and the Ugly", "Django Unchained", "True Grit", "Unforgiven", "The Hateful Eight", "Once Upon a Time in the West", "No Country for Old Men"]

def main():
    print("---Film Tavisyesi Uygulamasina Hoş Geldiniz---")
    print("Film Türleri:")
    print("1. Aksiyon Filmleri")
    print("2. Macera Filmleri")
    print("3. Komedi Filmleri")
    print("4. Korku Filmleri")
    print("5. Gerilim Filmleri")
    print("6. Animasyon Filmleri")
    print("7. Western Filmleri")
    secenek = int(input("Tavsiye almak istediginiz Film Türünü Tuşlayiniz: "))

    if secenek == 1:
        film = random.choice(aksiyon_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    elif secenek == 2:
        film = random.choice(macera_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    elif secenek == 3:
        film = random.choice(komedi_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    elif secenek == 4:
        film = random.choice(korku_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    elif secenek == 5:
        film = random.choice(gerilim_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    elif secenek == 6:
        film = random.choice(animasyon_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    elif secenek == 7:
        film = random.choice(western_filmleri)
        print(f"Rastgele Seçilen Fİlm Türünüz: {film}")
    else:
        print("Gecersiz Tuşlama!")

if __name__ == "__main__":
    main()
