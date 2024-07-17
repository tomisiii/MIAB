#importing the sql library
import pymysql

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
            database='drug'  # Corrected database name
        )
        print("Database connection established.")
        #message if connection was not established
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
#function to add drug info to the database
def add_drug(drug_info):
    global con
    try:
        if con is None:
            initialize_db()  # Initialize database connection if not already done

        if con:
            with con.cursor() as cursor:
                #sql code to insert data into database
                sql = '''
                INSERT INTO drug_info(name, quantity, price, category)
                VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(sql, (drug_info['name'], drug_info['quantity'], drug_info['price'], drug_info['category']))
            con.commit()
            print(f"{drug_info['name']} added to the database.")
    except pymysql.IntegrityError:
        print(f"{drug_info['name']} already exists in the database.")
    except pymysql.Error as e:
        print(f"Error adding drug: {e}")
        
        #function to remove drugs from database
def remove_drug(drug_info):
    global con

    if con is None:
        initialize_db()  # Initialize database connection if not already done

    if con:
        try:
            with con.cursor() as cursor:
                sql = '''
                DELETE FROM drug_info
                WHERE name = %s AND quantity = %s AND price = %s AND category = %s
                '''
                cursor.execute(sql, (drug_info['name'], drug_info['quantity'], drug_info['price'], drug_info['category']))
            con.commit()
            print(f"{drug_info['name']} removed from the database.")
        except pymysql.Error as e:
            print(f"Error removing drug: {e}")
            
#function to edit drug info within the database 
def edit_drug(drug_info):
    global con

    if con is None:
        initialize_db()  # Initialize database connection if not already done

    if con:
        try:
            with con.cursor() as cursor:
                #sql code to edit drug info
                sql = ''' 
                UPDATE drug_info
                SET quantity = %s, price = %s, category = %s
                WHERE name = %s
                '''
                cursor.execute(sql, (drug_info['quantity'], drug_info['price'], drug_info['category'], drug_info['name']))
            con.commit()
            print(f"{drug_info['name']} updated in the database.")
        except pymysql.Error as e:
            print(f"Error updating drug: {e}")
            
#function to  fetch and print all drug info
def print_drugs():
    global con

    if con is None:
        initialize_db()  # Initialize database connection if not already done

    if con:
        try:
            with con.cursor() as cursor:
                #basic sql code to perform selection within database
                sql = "SELECT * FROM drug_info"
                cursor.execute(sql)
                #calling the .fetchall() function to take all results and put them into the results variable
                results = cursor.fetchall()

                if not results:
                    print("No drugs found in the database.")
                else:
                    print("\nList of drugs in the database:")
                    print("------------------------------")
                    for row in results:
                        print(f"Name: {row[1]}")  # Assuming 'name' is the second column in your SELECT query result
                        print(f"Quantity: {row[2]}")  # Assuming 'quantity' is the third column
                        print(f"Price: {row[3]}")  # Assuming 'price' is the fourth column
                        print(f"Category: {row[4]}")  # Assuming 'category' is the fifth column
                        print("------------------------------")

        except pymysql.Error as e:
            print(f"Error fetching data: {e}")



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
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            category = input("Enter category: ")
            remove_drug({'name': name, 'quantity': quantity, 'price': price, 'category': category})
            
        if choice == '4':
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

if __name__ == "__main__":
    main()
