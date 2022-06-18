import string
import random
import datetime

from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData, Table, Column, String, Date

db = create_engine('sqlite:///movies2.db', echo=True)

meta = MetaData(db)

movies = Table('movies', meta,
                Column('title', String),
                Column('director', String),
                Column('release_date', Date)
            )

#ez a session
with db.connect() as conn:
    if not inspect(db).has_table('movies'):
        movies.create()    

    for i in range(10):
        # random szöveg generálása az angol abc betűíből
        title = "".join(random.choice(string.ascii_letters) for i in range(10))
        datum = random.randint(1980, 2022)

        insert_statement = movies.insert().values(title=title, 
                                    director="Ridley Scott", 
                                    release_date=datetime.datetime(datum, 5, 17))
        conn.execute(insert_statement)

    select_statement = movies.select()
    result_set = conn.execute(select_statement)

    for i in result_set:
        print(i)

    # delete_statement = movies.delete()
    # conn.execute(delete_statement)

    update_statement = movies.update().where(movies.c.release_date > datetime.datetime(2000, 1, 1)).values(director="Tanrantino")

    # OLTP  - Online Transactinal Processeing - Foodpanda, Netbank, Ügyfélkapu

    # Business Intelligence - BI - adattárház, data lake, lakehouse

    conn.execute(update_statement)
