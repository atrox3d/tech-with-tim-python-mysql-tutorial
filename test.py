from datetime import datetime

from database import db, cursor

def create_table_test():
    sql = """-- sql
        CREATE TABLE if not exists test(
            id int auto_increment primary key not null,
            name varchar(50) not null,
            created datetime not null,
            gender enum('M', 'F', 'O') not null
        )
    """
    cursor.execute(sql)


def insert_test(name:str, created:datetime, gender:str):
    cursor.execute("""-- sql
        insert into test (name, created, gender) values(%s, %s, %s)
    """, (name, created, gender))
    db.commit()