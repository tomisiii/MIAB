# from main import initialize_db
import pymysql
def edit_drug(drug_info):
   
    global con

    # if con is None:
    #     initialize_db()  # Initialize database connection if not already done

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