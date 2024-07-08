def amount():
    amount = []
    
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
    while True:
        