# from main import initialize_db
import pymysql
def add_drug(drug_info):
    global con
    try:
        # if con is None:
        #     initialize_db()  # Initialize database connection if not already done

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
        