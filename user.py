from database import db, cursor, drop_table

def create_table_user():
    cursor.execute("""-- sql
        create table if not exists user(
            id int primary key auto_increment,
            name varchar(50),
            username varchar(50),
            password varchar(50),
            email varchar(50)
        )
    """)

def create_users_data():
    names = 'roby fab cika'.split()
    usernames = 'rob chad cix'.split()
    passwords = '123 meow 456'.split()
    emails = [f'{name}@gmail.com' for name in names]
    users =list(zip(names, usernames, passwords, emails))
    return users

SQL_INSERT_USERS = """-- sql
    insert into user
    (name, username, password, email)
    values (%s, %s, %s, %s)
"""
def insert_user(name, username, password, email):
    cursor.execute(SQL_INSERT_USERS, (name, username, password, email))
    db.commit()

def insert_users(*users):
    cursor.executemany(SQL_INSERT_USERS, users)
    db.commit()

def setup_users(create:bool=True, drop:bool=True):
    if create:
        if drop:
            drop_table('user')
        create_table_user()
    
    users = create_users_data()
    insert_users(*users)
