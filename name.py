def name():
    # Initialize an empty list to store names (or drugs)
    drugs = []

    #prompt user to pick an option
    while True:
        print("\nMenu:")
        print("1. Add a drug")
        print("2. Remove a drug")
        print("3. Search for a drug")
        print("4. Edit a drug name")
        print("5. Print all drugs")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_drug(drugs)
        elif choice == '2':
            remove_drug(drugs)
        elif choice == '3':
            search_drug(drugs)
        
        elif choice == '4' :
            edit_drugs(drugs)
        elif choice == '5':
            print_drugs(drugs)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def add_drug(drugs):
    name = input("Enter the name of the drug to add: ").strip()
    if name in drugs:
        print(f"{name} is already in the list.")
    else:
        drugs.append(name)
        print(f"{name} added to the list.")

def remove_drug(drugs):
    name = input("Enter the name of the drug to remove: ").strip()
    if name in drugs:
        drugs.remove(name)
        print(f"{name} removed from the list.")
    else:
        print(f"{name} is not in the list.")

def search_drug(drugs):
    name = input("Enter the name of the drug to search: ").strip()
    if name in drugs:
        print(f"{name} found in the list.")
    else:
        print(f"{name} not found in the lit.")
def edit_drugs(drugs):
    current_name = input("Enter the current name of the drug to edit: ").strip()
    if current_name in drugs:
        new_name = input(f"Enter the new name for {current_name}: ").strip()
        if new_name != current_name:
            if new_name in drugs:
                print(f"{new_name} is already in the list.")
            else:
                index = drugs.index(current_name)
                drugs[index] = new_name
                print(f"Successfully edited {current_name} to {new_name}.")
        else:
            print("New name is the same as the current name. No changes made.")
    else:
        print(f"{current_name} is not in the list.")
        

def print_drugs(drugs):
    print("\nList of drugs:")
    for drug in drugs:
        print(drug)

name()