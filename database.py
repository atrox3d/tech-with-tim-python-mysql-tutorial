import mysql.connector

DATABASE = 'testdatabase'
db = mysql.connector.connect(
    host='localhost',
    user='user',
    password='123',
    database=DATABASE
)
cursor = db.cursor()

cursor.execute(f'create database if not exists {DATABASE}')

def drop_table(table:str):
    cursor.execute(f'drop table if exists {table}')

def test_cursor_iterator(sql:str, *params):
    cursor.execute(sql, params)

    print(cursor.statement)
    print(cursor.column_names)
    for item in cursor:
        print(f'iterator {item = }')

