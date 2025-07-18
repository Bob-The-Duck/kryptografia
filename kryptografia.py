from colorama import Fore, Style, init
from cryptography.fernet import Fernet
from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text

#====================================================#
# POBIERZ PACZKI ZASOBÓW W COMAND PROMPT
# pip install -r requirements.txt 
# w folderze znajdującym się ten skrypt
#====================================================#

# Inicjalizacja coloramy
init(autoreset=True)  # żeby kolor sam się resetował po każdym znaku

# Lista kolorów – będą się powtarzać w "fali"
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# Funkcja do wyświetlania kolorowego tekstu
def color_text(text):
    for i, sign in enumerate(text):  # każda litera z tekstu + jej indeks
        color = colors[i % len(colors)]  # kolor zmienia się co literę
        print(color + sign, end="")  # end="" – żeby nie było enterów między literami
    print()  # enter po całym tekście


def generate_key():  # funkcja do generowania klucza
    key = Fernet.generate_key()  # tworzymy klucz

    with open("klucz.key", "wb") as file:  # open(..., "wb") oznacza: otwórz plik do zapisu binarnego.
        # with automatycznie zamknie plik po zapisie.
        file.write(key)  # file.write(key) zapisuje klucz do pliku o nazwie klucz.key
    print("✅ Klucz został wygenerowany i zapisany jako 'klucz.key'")


def encrypt_message():
    # 1. Otwieramy plik z kluczem do odczytu (binarnie)
    with open("klucz.key", "rb") as file:
        key = file.read()  # wczytujemy klucz

    # 2. Tworzymy obiekt Fernet z wczytanym kluczem
    fernet = Fernet(key)

    # 3. Pytamy użytkownika o wiadomość do zaszyfrowania
    message = input("Wpisz wiadomość do zaszyfrowania: ")

    # 4. Zamieniamy wiadomość na bajty
    message_bajts = message.encode()

    # 5. Szyfrujemy wiadomość
    encrypted = fernet.encrypt(message_bajts)

    # 6. Zapisujemy szyfrogram do pliku
    with open("szyfrogram.txt", "wb") as file:
        file.write(encrypted)

    # 7. Wyświetlamy zaszyfrowany tekst
    print("🔒 Wiadomość została zaszyfrowana!")
    print("➡️  Zaszyfrowana wiadomość:")
    print(encrypted.decode())


def decrypt_message():  # definicja nowej funkcji
    with open("klucz.key", "rb") as file:  # Otwieramy plik z kluczem (klucz.key) w trybie binarnym ("rb")
        key = file.read()  # Czytamy cały klucz do zmiennej key.

    fernet = Fernet(key)  # Tworzymy obiekt Fernet – to nasze „urządzenie” do deszyfrowania, które zna ten klucz

    with open("szyfrogram.txt", "rb") as file:  # Otwieramy plik z zaszyfrowanym tekstem.
        cryptogram = file.read()

    try:
        decrypt = fernet.decrypt(cryptogram)  # Próba odszyfrowania
        print("✅ Wiadomość została odszyfrowana:")
        print(decrypt.decode())
    except Exception as e:
        print("❌ Błąd podczas odszyfrowywania:", e)






f = Figlet(font='small')# ustawiamy font na small
color_text(f.renderText('KRYPTOGRAFIA')) #generowanie tekstu w stylu ASCII
print() #odstęp
print("1 - Wygeneruj klucz")#opcja 1
print("2 - Zaszyfruj wiadomość")#opcja 2
print("3 - Odszyfruj wiadomość")#opcja 3

choose = input("Wybierz opcję: ")  # zapytanie użytkownika o opcję

# Obsługa wyboru
if choose == "1":
    generate_key()
elif choose == "2":
    encrypt_message()
elif choose == "3":
    decrypt_message()







