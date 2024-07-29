# from main import initialize_db
import pymysql
from main import csv

def print_drugs():
    
     global con

    #  if con is None:
    #     initialize_db()  # Initialize database connection if not already done

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
                        with open('main.csv', 'w', newline='') as file:
                            csv_writer = csv.writer(file)
                            csv_writer.writerow(['Name', 'Quantity', 'Price', 'Category'])
                            for row in results:
                                csv_writer.writerow([row[1], row[2], row[3], row[4]])

        except pymysql.Error as e:
            print(f"Error fetching data: {e}")
