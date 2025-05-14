def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
