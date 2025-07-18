# Projekt Kryptografia

## Opis Projektu

Ten projekt to prosta aplikacja w Pythonie, która umożliwia generowanie kluczy kryptograficznych, szyfrowanie wiadomości oraz ich deszyfrowanie. Wykorzystuje bibliotekę `cryptography` z implementacją symetrycznego szyfru Fernet, co zapewnia bezpieczeństwo przesyłanych danych. Aplikacja posiada również estetyczne elementy interfejsu, takie jak kolorowy tekst i banery ASCII, dzięki bibliotekom `colorama`, `pyfiglet` i `rich`.

## Funkcje

* **Generowanie klucza**: Tworzy unikalny klucz szyfrujący i zapisuje go do pliku `klucz.key`.
* **Szyfrowanie wiadomości**: Umożliwia wprowadzenie tekstu, który zostanie zaszyfrowany za pomocą wygenerowanego klucza i zapisany do pliku `szyfrogram.txt`.
* **Deszyfrowanie wiadomości**: Odczytuje zaszyfrowany tekst z pliku `szyfrogram.txt` i deszyfruje go za pomocą tego samego klucza, wyświetlając oryginalną wiadomość.

## Wymagania

Projekt wymaga Pythona 3.x oraz kilku bibliotek zewnętrznych.

## Instalacja

Aby uruchomić projekt, wykonaj następujące kroki:

1.  **Sklonuj repozytorium** (jeśli masz dostęp, w przeciwnym razie pobierz pliki):
    ```bash
    git clone [https://github.com/Bob-The-Duck/kryptografia.git](https://github.com/Bob-The-Duck/kryptografia.git)
    ```
2.  **Przejdź do katalogu projektu**:
    ```bash
    cd kryptografia
    ```
3.  **Zainstaluj wymagane biblioteki** za pomocą `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    Upewnij się, że Twój plik `requirements.txt` zawiera następujące pozycje:
    ```
    colorama
    cryptography
    pyfiglet
    rich
    ```

## Użycie

Po zainstalowaniu zależności, możesz uruchomić skrypt `kryptografia.py`:

```bash
python kryptografia.py
