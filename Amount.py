def amount():
    amount = []
    #trying to make the pop up menu to select option
    while True:
        print("\n MENU " )
        print("1. Record the Amount of the drugs")
        print("2. Edit the amount of the drugs")
        print("3. Quit ")
        
        
        choice = input("Enter your choice (1 or 2 ): ").strip()
        
        if choice == '1':
            record_amount(amount)
        elif choice == '2':
            edit_amount(amount)
        elif choice == '3':
            break
        else :
            print("This is an invalid option ")
            
def record_amount(amount):
    #a function to be able to record the amount of drugs by user
    while True:
        record_int_amount = float(input(("Please in put the Current amount of drugs available : ")))
        if record_int_amount == 0:
            print("There cannot be zero drugs ")
        else :
            amount.append(record_int_amount)
            print(f"There are now {record_int_amount:.2f} units available")
        
        
        
        
amount()