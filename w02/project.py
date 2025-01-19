# Milestone Requirements

# Ask for the price of a child's meal and an adult's meal
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask for the number of children and adults
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

# Final Requirements

# Ask for the sales tax rate
sales_tax_rate = float(input("What is the sales tax rate? "))

# Compute the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Compute the total price of the meal
total_price = subtotal + sales_tax

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total_price:.2f}")

# Ask for the payment amount
payment_amount = float(input("\nWhat is the payment amount? "))

# Compute the change
change = payment_amount - total_price

print(f"Change: ${change:.2f}")


# Creativity: Added drinks and tipping

# Ask if the user wants to include drinks
include_drinks = input("\nWould you like to add drinks? (yes/no): ").lower()
if include_drinks == "yes":
    drink_price = float(input("What is the price of a drink? "))
    num_drinks = int(input("How many drinks? "))
    drink_total = drink_price * num_drinks
    subtotal += drink_total
    print(f"Drinks Total: ${drink_total:.2f}")

# Ask if the user wants to include a tip
include_tip = input("\nWould you like to add a tip? (yes/no): ").lower()
if include_tip == "yes":
    tip_percentage = float(input("What percentage would you like to tip? "))
    tip_amount = (subtotal * tip_percentage) / 100
    total_price += tip_amount
    print(f"Tip Amount: ${tip_amount:.2f}")

# Recalculate totals after creativity additions
sales_tax = (subtotal * sales_tax_rate) / 100
total_price = subtotal + sales_tax

# Display final totals
print(f"\nUpdated Subtotal: ${subtotal:.2f}")
print(f"Updated Sales Tax: ${sales_tax:.2f}")
print(f"Updated Total: ${total_price:.2f}")

# Ask for the payment amount again
payment_amount = float(input("\nWhat is the payment amount? "))

# Compute and display the updated change
change = payment_amount - total_price
print(f"Updated Change: ${change:.2f}")
