from database import db, cursor, drop_table

def create_table_score():
    cursor.execute("""-- sql
        create table if not exists score(
            userid int primary key,
            game1 int default 0,
            game2 int default 0,
            foreign key(userid)
                references user(id)
        )
    """)

def create_scores_data():
    return [
        (45, 100),
        (30, 200),
        (46, 124),
    ]

SQL_INSERT_SCORE = """-- sql
    insert into score
    (userid, game1, game2)
    values (%s, %s, %s)
"""
def insert_score(userid, game1, game2):
    cursor.execute(SQL_INSERT_SCORE, (userid, game1, game2))
    db.commit()

def insert_scores(*scores):
    cursor.executemany(SQL_INSERT_SCORE, scores)
    db.commit()

def setup_scores(create:bool=True, drop:bool=True):
    if create:
        if drop:
            drop_table('score')
        create_table_score()
    
    scores = create_scores_data()
    insert_scores(*scores)
