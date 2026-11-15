from datetime import date
from fpdf import FPDF
from pathlib import Path

# --- Change these lines to your real information ---
my_name = "Ihr Name / Ihre Firma"
my_address = "Musterstrasse 1, 12345 Musterstadt"
my_tax_number = "Steuernummer: 12/345/67890"
my_payment_text = "Zahlbar innerhalb von 14 Tagen ohne Abzug."
my_iban = "IBAN: DE00 0000 0000 0000 0000 00"
# ---------------------------------------------------

customer = input("Kunde (customer name)? ")
counter_file = Path("counter.txt")

if counter_file.exists():
    last = int(counter_file.read_text())
else:
    last = 100

number = last + 1
counter_file.write_text(str(number))
print("Invoice number:", number)
today = date.today().strftime("%d.%m.%Y")

items = []

count = int(input("How many items? "))

for i in range(count):
    item_name = input("Name of item? ")
    item_price = float(input("Price? "))
    item_quantity = int(input("Quantity? "))
    items.append({"name": item_name, "price": item_price, "quantity": item_quantity})

mwst_rate = 0.19

pdf = FPDF()
pdf.add_page()


def write(text, size=12):
    pdf.set_font("Helvetica", size=size)
    pdf.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")


def row(a, b, c, d, bold=False):
    style = "B" if bold else ""
    pdf.set_font("Helvetica", style=style, size=11)
    pdf.cell(80, 8, a, border=1)
    pdf.cell(25, 8, b, border=1, align="R")
    pdf.cell(40, 8, c, border=1, align="R")
    pdf.cell(40, 8, d, border=1, align="R", new_x="LMARGIN", new_y="NEXT")


write(my_name)
write(my_address)
write(my_tax_number)
write("")
write(f"RECHNUNG {number}", 20)
write(f"Datum: {today}")
write(f"Kunde: {customer}")
write("")

row("Bezeichnung", "Menge", "Einzelpreis", "Gesamt", bold=True)

net_total = 0

for item in items:
    line = item["price"] * item["quantity"]
    row(item["name"], str(item["quantity"]), f"{item['price']:.2f}", f"{line:.2f}")
    net_total = net_total + line

mwst = net_total * mwst_rate

write("")
write(f"Netto:  {net_total:.2f} EUR")
write(f"MwSt:   {mwst:.2f} EUR")
write(f"Brutto: {net_total + mwst:.2f} EUR", 14)

write("")
write(my_payment_text, 11)
write(my_iban, 11)
write("Vielen Dank für Ihren Auftrag!", 11)

folder = Path("Rechnungen")
folder.mkdir(exist_ok=True)

file_name = f"Rechnung_{number}.pdf"
target_file = folder / file_name

if target_file.exists():
    print("STOP: this invoice already exists:", target_file)
else:
    pdf.output(str(target_file))
    print("PDF created:", target_file)