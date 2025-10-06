# FINE 3300 - Assignment 1
# Part 2: ExchangeRates class
# Author: Hamda Yusuf

import csv

class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.latest_rate = None
        self.read_latest_rate()

    def read_latest_rate(self):
        """Read the CSV and store the latest USD/CAD exchange rate"""
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            # The last row usually has the most recent data
            last_row = rows[-1]
            self.latest_rate = float(last_row["USD/CAD"])  # column name in Bank of Canada file

    def convert(self, amount, from_currency, to_currency):
        """Convert CAD <-> USD"""
        rate = self.latest_rate
        if from_currency.upper() == "CAD" and to_currency.upper() == "USD":
            return amount / rate
        elif from_currency.upper() == "USD" and to_currency.upper() == "CAD":
            return amount * rate
        else:
            raise ValueError("Currency must be CAD or USD")

# ---- Example user interaction ----
if __name__ == "__main__":
    filename = input("Enter the CSV filename: ")
    er = ExchangeRates(filename)

    amount = float(input("Enter the amount to convert: "))
    from_curr = input("Enter the currency you are converting from (CAD or USD): ")
    to_curr = input("Enter the currency you are converting to (CAD or USD): ")

    result = er.convert(amount, from_curr, to_curr)
    print(f"{amount:.2f} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")
