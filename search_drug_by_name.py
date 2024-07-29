# from main import initialize_db
import pymysql
def search_drug_by_name():
    global con
    
    # if con is None:
    #     initialize_db()  # Define this function to initialize your database connection
    
    if con:
        try:
            with con.cursor() as cursor:
                drug_name = input("Enter the name of the drug you want to search for: ")
                sql = "SELECT * FROM drug_info WHERE name = %s"
                cursor.execute(sql, (drug_name,))
                result = cursor.fetchone()

                if not result:
                    print(f"No drug named '{drug_name}' found in the database.")
                else:
                    print("\nInformation on drug in the database:")
                    print("------------------------------")
                    print(f"Name: {result[1]}")     # Adjust indexing based on your SQL query
                    print(f"Quantity: {result[2]}")
                    print(f"Price: {result[3]}")
                    print(f"Category: {result[4]}")
                    print("------------------------------")

        except pymysql.Error as e:
            print(f"Error fetching data: {e}")
            
