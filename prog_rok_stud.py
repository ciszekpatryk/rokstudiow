import os

def stworzenie_katalogu():
    nazwa = input("Podaj nazwę katalogu (np. Rok_1): ")
    try:
        os.makedirs(nazwa)
        print(f"Katalog '{nazwa}' został utworzony.")
    except FileExistsError:
        print(f"Katalog '{nazwa}' już istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

def wyswietlenie_katalogow():
    katalogi = [nazwa for nazwa in os.listdir() if os.path.isdir(nazwa)]
    if katalogi:
        print("Lista katalogów:")
        for katalog in katalogi:
            print(katalog)
    else:
        print("Brak katalogów w bieżącym katalogu roboczym.")

def edycja_katalogu():
    stara_nazwa = input("Podaj nazwę katalogu, który chcesz zmienić: ")
    if os.path.isdir(stara_nazwa):
        nowa_nazwa = input("Podaj nową nazwę katalogu: ")
        try:
            os.rename(stara_nazwa, nowa_nazwa)
            print(f"Katalog '{stara_nazwa}' został zmieniony na '{nowa_nazwa}'.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
    else:
        print(f"Katalog '{stara_nazwa}' nie istnieje.")

def usuniecie_katalogu():
    nazwa = input("Podaj nazwę katalogu, który chcesz usunąć: ")
    if os.path.isdir(nazwa):
        try:
            os.rmdir(nazwa)
            print(f"Katalog '{nazwa}' został usunięty.")
        except OSError:
            print(f"Katalog '{nazwa}' nie jest pusty lub wystąpił inny błąd.")
    else:
        print(f"Katalog '{nazwa}' nie istnieje.")

def menu():
    while True:
        print("\nZarządzanie Katalogami Roków Studiów")
        print("1. Tworzenie katalogu")
        print("2. Wyświetlenie listy katalogów")
        print("3. Edycja katalogu")
        print("4. Usunięcie katalogu")
        print("5. Wyjście")
        
        wybor = input("Wybierz opcję (1-5): ")

        if wybor == '1':
            stworzenie_katalogu()
        elif wybor == '2':
            wyswietlenie_katalogow()
        elif wybor == '3':
            edycja_katalogu()
        elif wybor == '4':
            usuniecie_katalogu()
        elif wybor == '5':
            print("Wyjście z programu.")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

# Uruchomienie programu
menu()
