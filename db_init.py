# run this to create an SQLite db ('data.db') with authorized users

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# id is an auto-incremented column
create_table_query = "CREATE TABLE clients (id, name text, email text, phone text," \
                     "address text, city text, postalcode text, country text)"
cursor.execute(create_table_query)

# id is an auto-incremented column
create_table_query = "CREATE TABLE users (id , username text, password text)"
cursor.execute(create_table_query)

insert_query = "INSERT INTO users VALUES (1, 'elad', 'password')"
cursor.execute(insert_query)

insert_query = "INSERT INTO clients VALUES (1, 'Elad Tzemach', 'eladtzemach@gmail.com', '613-444-0000', " \
               "'10 Cumberland St.', 'Ottawa', 'K1N 3J4', 'Canada')"
cursor.execute(insert_query)
insert_query = "INSERT INTO clients VALUES (2, 'John Smith', 'johns@gmail.com', '613-111-0000', " \
               "'14 Montreal Rd.', 'Ottawa', 'K1N 1E1', 'Canada')"
cursor.execute(insert_query)
insert_query = "INSERT INTO clients VALUES (3, 'Tom Rein', 'tomr@gmail.com', '613-222-0000', " \
               "'123 Blue Jays Rd.', 'Toronto', 'U6G 7R7', 'Canada')"
cursor.execute(insert_query)
insert_query = "INSERT INTO clients VALUES (4, 'Katie Jhonson', 'katiej@gmail.com', '613-000-0000', " \
               "'55 Sunland Dr.', 'Toronto', 'Q1Q 4J4', 'Canada')"
cursor.execute(insert_query)
insert_query = "INSERT INTO clients VALUES (5, 'Andrea Redford', 'andrear@gmail.com', '613-999-0000', " \
               "'41 Robert Bourassa Blvd.', 'Montreal', 'K18 J9G', 'Canada')"
cursor.execute(insert_query)

connection.commit()
connection.close()