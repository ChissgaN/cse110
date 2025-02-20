def display_menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item(cart, prices):
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    cart.append(item)
    prices.append(price)
    print(f"'{item}' has been added to the cart.")

def view_cart(cart, prices):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        for i, (item, price) in enumerate(zip(cart, prices), start=1):
            print(f"{i}. {item} - ${price:.2f}")

def remove_item(cart, prices):
    view_cart(cart, prices)
    if cart:
        try:
            index = int(input("\nWhich item would you like to remove? ")) - 1
            if 0 <= index < len(cart):
                removed_item = cart.pop(index)
                removed_price = prices.pop(index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def compute_total(prices):
    total = sum(prices)
    print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")

def main():
    cart = []
    prices = []
    
    print("Welcome to the Shopping Cart Program!")
    while True:
        display_menu()
        try:
            choice = int(input("Please enter an action: "))
            if choice == 1:
                add_item(cart, prices)
            elif choice == 2:
                view_cart(cart, prices)
            elif choice == 3:
                remove_item(cart, prices)
            elif choice == 4:
                compute_total(prices)
            elif choice == 5:
                print("Thank you. Goodbye.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
