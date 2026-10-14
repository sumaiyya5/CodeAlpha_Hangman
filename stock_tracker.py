# Stock Portfolio Tracker - CodeAlpha Task 2

stock_prices = {"AAPL": 180, "TSLA": 250}

total_investment = 0
results = []

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:")
for stock, price in stock_prices.items():
    print(stock, ": $", price)
print("Type 'done' when finished.\n")

while True:
    name = input("Enter stock name: ").upper().strip()

    if name == "DONE":
        break

    if name not in stock_prices:
        print("Stock not found. Choose AAPL or TSLA.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid whole number.\n")
        continue

    value = stock_prices[name] * quantity
    total_investment += value
    results.append(name + ": " + str(quantity) + " x $" + str(stock_prices[name]) + " = $" + str(value))
    print("Added!\n")

print("\n===== PORTFOLIO SUMMARY =====")
for line in results:
    print(line)
print("Total Investment: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    for line in results:
        file.write(line + "\n")
    file.write("Total Investment: $" + str(total_investment) + "\n")

print("Result saved to portfolio.txt")
