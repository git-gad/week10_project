from models import ContactCreate
import os
import time
from mysql.connector import connect, Error

def get_connection(retries=30, delay=1):
    host = os.getenv("DB_HOST", "db")
    user = os.getenv("DB_USER", "app_user")
    password = os.getenv("DB_PASS", "app_pass")
    port = int(os.getenv("DB_PORT", 3306))
    database = os.getenv("DB_NAME", "app_db")

    for i in range(retries):
        try:
            return connect(
                host=host,
                user=user,
                password=password,
                port=port,
                database=database
            )
        except Error as e:
            print(f"MySQL not ready ({i+1}/{retries}): {e}")
            time.sleep(delay)

    raise RuntimeError("MySQL not available")

conn = get_connection()
cursor = conn.cursor()

def get_all():
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    return rows

def create_contact(contact: ContactCreate):
    query = '''INSERT INTO contacts (first_name, last_name, phone_number) 
            VALUES (%s, %s, %s)'''
    data = (contact.first_name, contact.last_name, contact.phone_number)
    cursor.execute(query, data)
    id = cursor.lastrowid
    conn.commit()
    return id  
    
def update_contact(id: int, updated_contact: ContactCreate):
    query = '''UPDATE contacts 
            SET first_name = %s, last_name = %s, phone_number = %s
            WHERE id = %s'''
    data = (updated_contact.first_name, updated_contact.last_name, updated_contact.phone_number, id)
    cursor.execute(query, data)
    conn.commit()
    
def del_contact(id: int):
    query = '''DELETE FROM contacts 
            WHERE id = %s'''
    cursor.execute(query, (id,))
    conn.commit()