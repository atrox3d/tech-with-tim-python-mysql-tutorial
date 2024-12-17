from datetime import datetime

from database import (
    db, 
    cursor,
    drop_table,
    test_cursor_iterator
)

from user import (
    create_table_user,
    create_users_data,
    insert_user
)

from score import (
    create_table_score,
    create_scores_data,
    insert_score
)

if __name__ == "__main__":
    drop_table('score')
    drop_table('user')
    create_table_user()
    create_table_score()

    users = create_users_data()
    scores = create_scores_data()
    
    for user, score in zip(users, scores):
        last_id = insert_user(*user)
        insert_score(last_id, *score)
    
    cursor.execute("""-- sql
        select *
        from user inner join score
        on user.id = score.userid
    """)

    for row in cursor:
        print(row)
