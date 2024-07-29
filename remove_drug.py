# from main import initialize_db
import pymysql
def remove_drug(drug_info):
    global con

    # if con is None:
    #     initialize_db()  # Initialize database connection if not already done

    if con:
        try:
            with con.cursor() as cursor:
                sql = '''
                DELETE FROM drug_info
                WHERE name = %s 
                '''
                cursor.execute(sql, (drug_info['name']))
            con.commit()
            print(f"{drug_info['name']} removed from the database.")
        except pymysql.Error as e:
            print(f"Error removing drug: {e}")