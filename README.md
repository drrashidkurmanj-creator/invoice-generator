# Invoice Generator (Rechnung)

A small Python tool that creates German invoices (*Rechnung*) as **PDF** files, with automatic invoice numbering and 19% VAT (*MwSt*).

## What it does

- Asks for the customer name and the invoice items (name, price, quantity)
- Calculates net total, 19% VAT and gross total
- Creates a PDF invoice with a table
- Numbers the invoices automatically (101, 102, 103, ...)
- Saves the PDF in a folder called `Rechnungen`
- Never overwrites an existing invoice

## Example output

See the sample invoice: [Rechnung_110.pdf](Rechnung_110.pdf)

The sample uses **made-up data** (customer: "Mustermann GmbH"). The sender name, address, tax number and IBAN in the sample are placeholders.

## How to use

1. Install Python 3 and the library:

   ```
   pip install fpdf2
   ```

2. Open `rechnung.py` and change the five lines at the top (name, address, tax number, payment text, IBAN).
3. Run:

   ```
   python rechnung.py
   ```

4. Answer the questions. The invoice is saved as `Rechnungen/Rechnung_<number>.pdf`.

The last invoice number is stored in a small file called `counter.txt` (created automatically).

## Customization

Every business needs slightly different invoices. The layout, items and VAT rate can be adapted.

## Note

This is a demo tool. It does not replace tax advice. Please check the legal requirements for invoices with a tax advisor.

## Tech

Python, fpdf2

---

## Auf Deutsch

Ein kleines Python-Programm, das **Rechnungen als PDF** erstellt: mit automatischer Rechnungsnummer, Tabelle und 19 % MwSt. Die Beispieldaten sind frei erfunden. Dieses Programm ersetzt keine steuerliche Beratung.
