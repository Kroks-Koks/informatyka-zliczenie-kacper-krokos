# produkty kroee sa juz w magazynie i ich ilosci
magazyn = {
    "CPU":5,
    "gpu": 5,
    "RAM": 5,
    "ROM": 5,
    "zasilacz": 5,
    "obudowa": 5,
    "chlodzenie CPU": 5,
    "pasta termoprzewodzaca": 5,
}


def wyswietl_stan():
    """wysiwetl produkty i ich ilosc"""
    print("\n--- AKTUALNY STAN MAGAZYNOWY ---")
    if not magazyn:
        print("Magazyn jest pusty.")
    else:
        for produkt, ilosc in magazyn.items():
            print(f"• {produkt}: {ilosc} szt.")
    print("--------------------------------")


def dodaj_produkt():
    """dodawanie produktu i ich ilosc"""
    produkt = input("Podaj nazwę produktu: ").strip().capitalize()
    try:
        ilosc = int(input(f"Podaj ilość dla {produkt}: "))
        if ilosc < 0:
            print("Błąd: Ilość nie może być ujemna!")
            return

        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc
        print(f"Sukces: Dodano {ilosc} szt. produktu {produkt}.")
    except ValueError:
        print("Błąd: Musisz podać liczbę całkowitą!")


def wydaj_produkt():
    """Zmniejsza stan o dana liczbe"""
    produkt = input("Podaj nazwę produktu do wydania: ").strip().capitalize()
    if produkt not in magazyn:
        print("Błąd: Brak takiego produktu w bazie.")
        return

    try:
        ilosc = int(input(f"Ile sztuk '{produkt}' chcesz wydać?: "))
        if ilosc < 0:
            print("Błąd: Ilość nie może być ujemna!")
            return

        if ilosc > magazyn[produkt]:
            print(f"Błąd: Za mało towaru! W magazynie zostało tylko {magazyn[produkt]} szt.")
        else:
            magazyn[produkt] -= ilosc
            print(f"Sukces: Wydano {ilosc} szt. {produkt}.")
            # usuwanie produktu jezeli jest go 0 w magazynie
            if magazyn[produkt] == 0:
                del magazyn[produkt]
    except ValueError:
        print("Błąd: Musisz podać liczbę całkowitą!")


def menu():
    while True:
        print("\n=== SYSTEM MAGAZYNOWY ===")
        print("1. Wyświetl stan magazynu")
        print("2. Przyjmij towar (Dodaj / Zwiększ)")
        print("3. Wydaj towar (Zmniejsz)")
        print("4. Wyjście")

        wybor = input("Wybierz opcję (1-4): ").strip()

        if wybor == "1":
            wyswietl_stan()
        elif wybor == "2":
            dodaj_produkt()
        elif wybor == "3":
            wydaj_produkt()
        elif wybor == "4":
            print("Zamykanie programu. Do widzenia!")
            break
        else:
            print("Niepoprawny wybór! Wybierz cyfrę od 1 do 4.")


if __name__ == "__main__":
    menu()