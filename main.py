#importing the sql library
from os import name, system
import pymysql
import csv
import add_drug
import remove_drug
import edit_drug
import search_drug_by_category
import search_drug_by_name
import print_drugs
# Define a global connection object
con = None
#function to initialize the database
def initialize_db():
    global con
    try:
        con = pymysql.connect(
            host='localhost',
            user='root',
            #no password hence no password parameter
            database='miab'  # Corrected database name
        )
        print("Database connection established.")
        #message if connection was not established
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")




#defining the main function
def main():
    #the initialize_db() function is only called if the main() function is called
    initialize_db()
    
    #while loop to keep printing the pop-up menu
    while True:
        print("\nMenu:")
        print("1. Add drug information") #done
        print("2. Remove drug information") #done
        print("3. Search for drug information") #yet to do
        print("4. Edit drug information") #done
        print("5. Print all drug information") #done
        print("6. Quit") #done
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name of the drug: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            category = input("Enter category: ")
            add_drug({'name': name, 'quantity': quantity, 'price': price, 'category': category})
            
        if choice == '2':
            name = input("Enter the name of the drug: ")
            # quantity = int(input("Enter quantity: "))
            # price = float(input("Enter price: "))
            # category = input("Enter category: ")
            # remove_drug({'name': name, 'quantity': quantity, 'price': price, 'category': category})
            remove_drug({'name': name})
            
        if choice == '3':
             prompt = input("Would you like to search for drug by category or name  ")
             if prompt == 'name':
                 search_drug_by_name()
             elif prompt == 'category':
                 search_drug_by_category()
                
                 
             
            
            
        if choice == '4':
            clear()
            print_drugs()
            
            name = input("Enter the name of the drug: ")
            
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            category = input("Enter category: ")
            edit_drug({'name': name, 'quantity': quantity, 'price': price, 'category': category})
        if choice == '5':
            print_drugs()
           

        elif choice == '6':
            break

    if con:
        con.close()
        print("Database connection closed.")

def clear():
    if name == 'nt':
         _ = system('cls')


if __name__ == "__main__":
    main()

