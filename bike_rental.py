import json
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Zmienna globalna dla katalogu danych
DATA_DIR = "data"

# Funkcja tworząca katalog 'data', jeśli nie istnieje
def ensure_data_directory():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

# Funkcja do obliczania kosztu wynajmu
def calculate_cost(rental_duration):
    cost_per_hour = 10  # Cena za godzinę
    return rental_duration * cost_per_hour

# Funkcja do zapisywania wynajmu do pliku
def save_rental(rental):
    ensure_data_directory()
    rentals_file = os.path.join(DATA_DIR, "rentals.json")
    
    if not os.path.exists(rentals_file):
        rentals = []
    else:
        with open(rentals_file, "r") as file:
            rentals = json.load(file)

    rentals.append(rental)

    with open(rentals_file, "w") as file:
        json.dump(rentals, file, indent=4)

# Funkcja wynajmu roweru
def rent_bike(customer_name, rental_duration):
    total_cost = calculate_cost(rental_duration)
    rental = {
        "customer_name": customer_name,
        "rental_duration": rental_duration,
        "total_cost": total_cost
    }
    save_rental(rental)
    print(f"{customer_name} wynajął rower na {rental_duration} godzin. Koszt: {total_cost} zł.")

# Funkcja do odczytu wynajmów
def load_rentals():
    ensure_data_directory()
    rentals_file = os.path.join(DATA_DIR, "rentals.json")
    
    if not os.path.exists(rentals_file):
        print("Brak wynajmów.")
        return

    with open(rentals_file, "r") as file:
        rentals = json.load(file)

    for rental in rentals:
        print(f"{rental['customer_name']} wynajął rower na {rental['rental_duration']} godzin. Koszt: {rental['total_cost']} zł.")

# Funkcja do anulowania wynajmu
def cancel_rental(customer_name):
    ensure_data_directory()
    rentals_file = os.path.join(DATA_DIR, "rentals.json")
    
    if not os.path.exists(rentals_file):
        print("Brak wynajmów.")
        return

    with open(rentals_file, "r") as file:
        rentals = json.load(file)

    rentals = [rental for rental in rentals if rental["customer_name"] != customer_name]

    with open(rentals_file, "w") as file:
        json.dump(rentals, file, indent=4)

    print(f"Wynajem {customer_name} został anulowany.")

# Funkcja do generowania raportu dziennego
def generate_daily_report():
    ensure_data_directory()
    today = datetime.now().strftime("%Y-%m-%d")
    report_file = os.path.join(DATA_DIR, f"daily_report_{today}.json")
    rentals_file = os.path.join(DATA_DIR, "rentals.json")
    
    if not os.path.exists(rentals_file):
        print("Brak wynajmów do raportu.")
        return

    with open(rentals_file, "r") as file:
        rentals = json.load(file)

    with open(report_file, "w") as file:
        json.dump({"date": today, "rentals": rentals}, file, indent=4)

    print(f"Raport dzienny zapisany do {report_file}.")

# Funkcja do wysyłania faktury e-mail
def send_rental_invoice_email(customer_email, rental_details):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Twój e-mail
    sender_password = "your_password"     # Twoje hasło do konta e-mail

    subject = "Faktura za wynajem roweru"
    body = (f"Dzień dobry {rental_details['customer_name']},\n\n"
            f"Koszt wynajmu: {rental_details['total_cost']} zł.\n"
            f"Czas wynajmu: {rental_details['rental_duration']} godz.\n\n"
            "Pozdrawiamy,\nZespół Wynajmu Rowerów")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = customer_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print(f"Faktura wysłana na {customer_email}.")
    except smtplib.SMTPException as e:
        print(f"Błąd przy wysyłaniu e-maila: {e}")

# Główna część programu
if __name__ == "__main__":
    while True:
        print("\n1. Wynajmij rower")
        print("2. Wyświetl wynajmy")
        print("3. Anuluj wynajem")
        print("4. Generuj raport dzienny")
        print("5. Wyślij fakturę")
        print("6. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Podaj imię i nazwisko: ")
            try:
                duration = int(input("Podaj czas wynajmu w godzinach: "))
                rent_bike(name, duration)
            except ValueError:
                print("Wprowadź poprawny czas wynajmu.")
        elif choice == "2":
            load_rentals()
        elif choice == "3":
            name = input("Podaj imię klienta do anulowania: ")
            cancel_rental(name)
        elif choice == "4":
            generate_daily_report()
        elif choice == "5":
            email = input("Podaj adres e-mail: ")
            name = input("Podaj imię klienta: ")
            rental = {"customer_name": name, "rental_duration": 5, "total_cost": 50}
            send_rental_invoice_email(email, rental)
        elif choice == "6":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór.")
