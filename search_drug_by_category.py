# from main import initialize_db
import pymysql
def search_drug_by_category():
       global con
    
    #    if con is None:
    #     initialize_db()  # Define this function to initialize your database connection
    
       if con:
        try:
            with con.cursor() as cursor:
                drug_category = input("Enter the category of the drugs you want to search for: ")
                sql = "SELECT * FROM drug_info WHERE category = %s"
                cursor.execute(sql, (drug_category,))
                result = cursor.fetchall()

                if not result:
                    print(f"No drug named '{drug_category}' found in the database.")
                else:
                    for row in result:
                     print(f"\nInformation on drug in the database by the category {drug_category}:")
                     print("------------------------------")
                     print(f"Name: {row[1]}")     # Adjust indexing based on your SQL query
                     print(f"Quantity: {row[2]}")
                     print(f"Price: {row[3]}")
                     print(f"Category: {row[4]}")
                     print("------------------------------")

        except pymysql.Error as e:
            print(f"Error fetching data: {e}")

