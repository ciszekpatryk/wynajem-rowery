# Aplikacja do wynajmu rowerów
### Aplikacja bike_rental.py umożliwia zarządzanie wynajmem rowerów, oferując następujące funkcje:

### 1. Wynajem rowerów
- Klient może wynająć rower na określoną liczbę godzin.
- Koszt wynajmu jest automatycznie obliczany na podstawie zadanej ceny za godzinę.
- Szczegóły wynajmu są zapisywane do pliku `data/rentals.json`.
### 2. Wyświetlanie aktualnych wynajmów
- Możliwość przeglądania wszystkich aktywnych wynajmów zapisanych w systemie.
- Informacje zawierają:
  - Imię klienta.
  - Liczbę godzin wynajmu.
  - Całkowity koszt wynajmu.
### 3. Anulowanie wynajmu
- Klient może anulować swój wynajem, podając swoje imię.
- Po anulowaniu dane wynajmu są usuwane z pliku `data/rentals.json`.
### 4. Generowanie raportów dziennych
- Aplikacja umożliwia zapisanie raportu dziennego wszystkich wynajmów w pliku `data/daily_reports/daily_report_<data>.json`.
- Plik zawiera:
  - Datę raportu.
  - Listę wszystkich wynajmów zapisanych w systemie.
### 5. Wysyłanie faktur e-mail
- System może wysłać e-mail z fakturą za wynajem roweru do klienta.
- Faktura zawiera szczegóły wynajmu:
  - Imię klienta.
  - Czas trwania wynajmu.
  - Koszt całkowity.

---

# Używanie programu
Po uruchomieniu aplikacji na ekranie pojawi się menu główne z listą wyboru dostępnych opcji:
```markdown
1. Wynajmij rower
2. Wyświetl wynajmy
3. Anuluj wynajem
4. Generuj raport dzienny
5. Wyślij fakturę
6. Zakończ
```

## Szczegółowe omówienie każdej z opcji:
### 1. Wynajmij rower
  - Po wybraniu tej opcji możemy podać imię i nazwisko klienta, wraz z czasem wynajmu. Obliczony zostanie całkowity koszt wynajmu, a szczegóły będą zapisane w pliku `data/rentals.json`.
### 2. Wyświetl wynajmy
  - Program odczytuje dane z pliku `data/rentals.json` i wyświetla listę aktualnych wynajmów, w przypadku braku wynajmów wyświetli stosowną informację.
### 3. Anuluj wynajem
  - W tej opcji po podaniu imienia i nazwiska klienta, program usunie odpowiedni wynajem z pliku `data/rentals.json`, po czym wyświetli potwierdzenie wykonania operacji. W przypadku braku podanego klienta, program poinformuje o błędzie
### 4. Generuj raport dzienny
  - Program odczytuje dane z `data/rentals.json`, a następnie tworzy plik raportu dziennego w katalogu `data/daily_reports/` o nazwie `daily_report_<data>.json`. Jeśli brakuje wynajmów, program poinformuje, że nie ma danych do raportu.
### 5. Wyślij fakturę
  - Po wybraniu tej opcji należy podać adres e-mail klienta oraz imię klienta, dla którego ma być wysłana faktura. Program następnie przygotuje treść faktury na podstawie przykładowych danych, a następnie wyśle fakturę na podany adres e-mail. W przypadku błędów (np. brak połączenia z Internetem lub niewłaściwe dane e-mail), program wyświetli odpowiedni komunikat.
### 6. Zakończ
  - Program zakończy działanie i wyświetli komunikat "*Do widzenia!*".

---

# Konfigurowanie Google Calendar

### 1. Utwórz projekt w Google Cloud Console:
  - Przejdź do Google Cloud Console.
  - Utwórz nowy projekt.
### 2. Włącz API Google Calendar:
  - Przejdź do sekcji API & Services > Library.
  - Wyszukaj "Google Calendar API" i włącz je dla swojego projektu.
### 3. Utwórz dane uwierzytelniające:
  - Przejdź do API & Services > Credentials.
  - Utwórz dane uwierzytelniające typu OAuth 2.0 Client IDs.
  - Pobierz plik credentials.json.
### 4. Zainstaluj wymagane biblioteki w Pythonie: Aby połączyć się z Google Calendar API, zainstaluj wymagane biblioteki:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### 5. W Pythonie musisz uwierzytelnić się za pomocą OAuth 2.0, aby uzyskać dostęp do kalendarza użytkownika. Użyj pliku credentials.json, który pobrałeś z Google Cloud Console, a następnie dodać integrację z Google Calendar do skryptu.

---

# Wysyłanie e-maili
Aby wysyłać e-maile z fakturą za wynajem roweru należy w skrypcie podać swój adres e-mail oraz odpowiednie hasło w miejscu `sender_email` oraz `sender_password`:
```python
def send_rental_invoice_email(customer_email, rental_details):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Twój e-mail
    sender_password = "your_password"     # Twoje hasło do konta e-mail
```
