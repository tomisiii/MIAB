def price():
    prices = []
    
    while True:
        print("\nMenu:")
        print("1. Enter a price")
        print("2. Remove a Price")
        print("3. Edit a price")
        print("4. Search for a Price")
        print("5. Print all prices")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            enter_price(prices)
        elif choice == '2':
            remove_price(prices)
        elif choice == '3':
            edit_price(prices)
        elif choice == '4':
            search_price(prices)
        elif choice == '5':
            print_price(prices)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def enter_price(prices):
    while True:
        try:
            price_str = input("Enter the price: ").strip()
            entered_price = float(price_str)
            prices.append(entered_price)
            print(f"The price ${entered_price:.2f} has been added.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def remove_price(prices):
    if not prices:
        print("The list of prices is empty.")
        return
    
    print("Current prices:")
    print_prices(prices)
    try:
        index = int(input("Enter the index of the price to remove: "))
        if 0 <= index < len(prices):
            removed_price = prices.pop(index)
            print(f"The price ${removed_price:.2f} has been removed.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def edit_price(prices):
    if not prices:
        print("The list of prices is empty.")
        return
    
    print("Current prices:")
    print_prices(prices)
    try:
        index = int(input("Enter the index of the price to edit: "))
        if 0 <= index < len(prices):
            new_price_str = input("Enter the new price: ").strip()
            new_price = float(new_price_str)
            prices[index] = new_price
            print(f"The price at index {index} has been updated to ${new_price:.2f}.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the price.")

def search_price(prices):
    if not prices:
        print("The list of prices is empty.")
        return
    
    search_value_str = input("Enter the price to search for: ").strip()
    try:
        search_value = float(search_value_str)
        found_indices = [i for i, price in enumerate(prices) if price == search_value]
        if found_indices:
            print(f"The price ${search_value:.2f} was found at indices:", found_indices)
        else:
            print(f"The price ${search_value:.2f} was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number to search.")

def print_price(prices):
    if not prices:
        print("The list of prices is empty.")
    else:
        print("Current prices:")
        print_prices(prices)

def print_prices(prices):
    for i, price in enumerate(prices):
        print(f"{i}: ${price:.2f}")

# Call the main function to start the program
price()
