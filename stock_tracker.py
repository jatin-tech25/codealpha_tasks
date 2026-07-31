"""
Stock Portfolio Tracker
------------------------
A simple command-line tool that lets a user enter stock names and
quantities, looks up prices from a hardcoded dictionary, calculates
the total investment value, and optionally saves the result to a
.txt or .csv file.
"""

import csv
from datetime import datetime

# ------------------------------------------------------------------
# Hardcoded stock prices (in USD). Add/edit as needed.
# ------------------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420,
    "NFLX": 680,
    "META": 500,
}


def get_portfolio_input():
    """
    Prompt the user for stock names and quantities.
    Returns a list of dicts: [{"symbol": "AAPL", "quantity": 10}, ...]
    """
    portfolio = []
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Type 'done' as the stock name when you're finished.\n")

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found in price list. Please try again.\n")
            continue

        qty_input = input(f"Enter quantity of {symbol}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  Invalid quantity. Please enter a whole number.\n")
            continue

        portfolio.append({"symbol": symbol, "quantity": quantity})
        print(f"  Added: {quantity} share(s) of {symbol}\n")

    return portfolio


def calculate_totals(portfolio):
    """
    Given a list of {"symbol", "quantity"}, compute per-stock value
    and total investment. Returns (rows, grand_total) where rows is
    a list of dicts with symbol, quantity, price, value.
    """
    rows = []
    grand_total = 0.0

    for item in portfolio:
        symbol = item["symbol"]
        quantity = item["quantity"]
        price = STOCK_PRICES[symbol]
        value = price * quantity
        grand_total += value

        rows.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value,
        })

    return rows, grand_total


def display_summary(rows, grand_total):
    """Print a formatted summary of the portfolio to the console."""
    print("\n=== Portfolio Summary ===")
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<12}")
    print("-" * 38)
    for row in rows:
        print(f"{row['symbol']:<8}{row['quantity']:<8}"
              f"${row['price']:<9}${row['value']:<11.2f}")
    print("-" * 38)
    print(f"Total Investment Value: ${grand_total:,.2f}\n")


def save_to_file(rows, grand_total):
    """
    Ask the user if they want to save the results, and in what
    format (.txt or .csv). Writes the file if requested.
    """
    choice = input("Save results to a file? (y/n): ").strip().lower()
    if choice != "y":
        print("Results not saved.")
        return

    file_format = input("Choose format - txt or csv: ").strip().lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for row in rows:
                writer.writerow([row["symbol"], row["quantity"],
                                  row["price"], f"{row['value']:.2f}"])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", f"{grand_total:.2f}"])
        print(f"Saved to {filename}")

    elif file_format == "txt":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, mode="w") as f:
            f.write("=== Portfolio Summary ===\n")
            f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<12}\n")
            f.write("-" * 38 + "\n")
            for row in rows:
                f.write(f"{row['symbol']:<8}{row['quantity']:<8}"
                         f"${row['price']:<9}${row['value']:<11.2f}\n")
            f.write("-" * 38 + "\n")
            f.write(f"Total Investment Value: ${grand_total:,.2f}\n")
        print(f"Saved to {filename}")

    else:
        print("Unrecognized format. Skipping save.")


def main():
    portfolio = get_portfolio_input()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    rows, grand_total = calculate_totals(portfolio)
    display_summary(rows, grand_total)
    save_to_file(rows, grand_total)


if __name__ == "__main__":
    main()