from datetime import datetime
from database import (
    db, 
    cursor,
    drop_table,
    test_cursor_iterator
)
from person import (
    create_table_person, 
    insert_person,
    get_persons
)

from test import(
    create_table_test,
    insert_test
)

if __name__ == "__main__":
    drop_table('person')
    create_table_person()
    test_cursor_iterator("""-- sql
        describe person
    """)

    insert_person('fab', 12)
    insert_person('bob', 54)

    get_persons()

    drop_table('test')
    create_table_test()

    insert_test('bob', datetime.now(), 'M')
    insert_test('fab', datetime.now(), 'O')

    cursor.execute('select id, name from test where gender = "M" order by id desc')
    for row in cursor:
        print(row)
    
    cursor.execute('describe test')
    while db.unread_result:
        print(cursor.fetchone())
    
    cursor.execute("""-- sql
            alter table test
            add column food varchar(50)
        """)
    
    cursor.execute("""-- sql
            alter table test
            drop column food
        """)
    
    cursor.execute("""-- sql
            alter table test
            change name first_name varchar(50)
        """)
    
