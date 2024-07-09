def main():
    # Initialize an empty dictionary to store drugs information
    drugs = {}

    def add_drug(drugs):
        #FUNCTION TO  ADD DRUGS
        name = input("Enter the name of the drug: ")
        if name in drugs:
            print(f"{name} is already in the list.")
        else:
            drugs[name] = {
                #STORING THE OTHER VARIABLES WITHIN THE INITIAL NAME VARIABLE
                "Quantity": int(input("Enter quantity: ")),
                "Price": float(input("Enter price: ")),
                "Category": input("Enter category: ")
            }
            print(f"{name} added to the list.")

    def remove_drug(drugs):
        #FUNCTION TO DELETE A DRUG FROM THE DICTIONARY
        #THINK OF WHETHER TO REMOVE A CERTAIN VARIABLE 
        name = input("Enter the name of the drug to remove: ")
        if name in drugs:
            del drugs[name]
            print(f"{name} removed from the list.")
        else:
            print(f"{name} is not in the list.")

    def search_drug(drugs):
        #FUNCTION TO SEARCH WITHIN THE DICTIONARY
        name = input("Enter the name of the drug to search: ")
        if name in drugs:
            print(f"Name: {name}")
            print(f"Quantity: {drugs[name]['Quantity']}")
            print(f"Price: {drugs[name]['Price']}")
            print(f"Category: {drugs[name]['Category']}")
        else:
            print(f"{name} is not found in the list.")

    def edit_drug(drugs):
        name = input("Enter the name of the drug to edit: ")
        if name in drugs:
            print(f"Current information for {name}:")
            print(f"Quantity: {drugs[name]['Quantity']}")
            print(f"Price: {drugs[name]['Price']}")
            print(f"Category: {drugs[name]['Category']}")
            drugs[name]["Quantity"] = int(input("Enter new quantity: "))
            drugs[name]["Price"] = float(input("Enter new price: "))
            drugs[name]["Category"] = input("Enter new category: ")
            print(f"{name} information updated.")
        else:
            print(f"{name} is not in the list.")

    def print_drugs(drugs):
        if not drugs:
            print("No drugs in the list.")
        else:
            print("List of drugs:")
            for name, info in drugs.items():
                print(f"Name: {name}")
                print(f"Quantity: {info['Quantity']}")
                print(f"Price: {info['Price']}")
                print(f"Category: {info['Category']}")
                print("--------------------------")

    while True:
        print("\nMenu:")
        print("1. Add drug information")
        print("2. Remove drug information")
        print("3. Search for drug information")
        print("4. Edit drug information")
        print("5. Print all drug information")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_drug(drugs)
        elif choice == '2':
            remove_drug(drugs)
        elif choice == '3':
            search_drug(drugs)
        elif choice == '4':
            edit_drug(drugs)
        elif choice == '5':
            print_drugs(drugs)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
