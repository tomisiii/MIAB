
import pymysql

# Define a global connection object
con = None

def initialize_db():
    global con
    try:
        con = pymysql.connect(
            host='localhost',
            user='root',
            database='drug'  # Corrected database name
        )
        print("Database connection established.")
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")

def add_drug(drug_info):
    global con
    try:
        if con is None:
            initialize_db()  # Initialize database connection if not already done

        if con:
            with con.cursor() as cursor:
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

       
    

def main():
    initialize_db()

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
           

        elif choice == '6':
            break

    if con:
        con.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
