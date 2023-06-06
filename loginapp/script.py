import psycopg2
import os

import time




class DatabaseManpasswordr:
    def __init__(self, database_email):
        self.conn = psycopg2.connect(database_email)
        self.cursor = self.conn.cursor()

    def create_table(self):
        start_time=time.time()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_data
                            (id SERIAL PRIMARY KEY,
                           email TEXT NOT NULL,
                            password TEXT NOT NULL)
                           ''')
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to create table is {end_time-start_time} seconds")
        

    def insert_data(self):
        start_time=time.time()
        user_data = []
        while True:
            email = input("Enter the email: ")
            password = input("Enter the password: ")
            user_data.append((email, password))
            if input("Do you want to add more data? (y/n)") == 'n':
                break
        self.cursor.executemany('INSERT INTO user_data (email, password) VALUES (%s, %s)', user_data)
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to insert data is {end_time-start_time} seconds")
     

    def delete_data(self):
        start_time=time.time()
        user_id = input("Enter the id: ")
        self.cursor.execute('DELETE FROM user_data WHERE id = %s', (user_id,))
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to delete data is {end_time-start_time} seconds")
      

    def update_data(self):
        start_time=time.time()
        user_id = input("Enter the id: ")
        user_email = input("Enter the email: ")
        user_password = input("Enter the password: ")
        self.cursor.execute('UPDATE user_data SET email = %s, password = %s WHERE id = %s', (user_email, user_password, user_id))
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to update data is {end_time-start_time} seconds")

    def view_all_data(self):
        start_time=time.time()
        self.cursor.execute('SELECT * FROM user_data')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to view all data is {end_time-start_time} seconds")
        
    def delete_all_data(self):
        start_time=time.time()
        self.cursor.execute('DELETE FROM user_data')
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to delete all data is {end_time-start_time} seconds")

    def view_single_data(self):
        start_time=time.time()
        user_id = input("Enter the id: ")
        self.cursor.execute('SELECT * FROM user_data WHERE id = %s', (user_id,))
        row = self.cursor.fetchone()
        print(row)
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to view single data is {end_time-start_time} seconds")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    database_manpasswordr = DatabaseManpasswordr(f'dbname=postgres user=postgres password= mahima@123 host=localhost port=5432')
    while True:
        print("1. Insert data", "2. Delete data", "3. Update data", "4. View all data", "5. Delete all data",
              "6. View single data", "7. Exit", sep="\n")
        x = int(input("Enter the option: "))

        if x == 1:
            database_manpasswordr.create_table()
            database_manpasswordr.insert_data()
        elif x == 2:
            database_manpasswordr.delete_data()
        elif x == 3:
            database_manpasswordr.update_data()
        elif x == 4:
            database_manpasswordr.view_all_data()
        elif x == 5:
            database_manpasswordr.delete_all_data()
        elif x == 6:
            database_manpasswordr.view_single_data()
        else:
            database_manpasswordr.close_connection()
            exit()