from database import db, cursor

def create_table_person():
    sql = """-- sql
        CREATE TABLE if not exists person(
            personid int auto_increment primary key,
            name varchar(50),
            age smallint UNSIGNED
        )
    """
    cursor.execute(sql)


def insert_person(name:str, age:int):
    cursor.execute("""-- sql
        insert into person (name, age) values(%s, %s)
    """, (name, age))
    db.commit()


def get_persons():
    cursor.execute("""-- sql
        select * from person
    """)
    for row in cursor:
        print(row)