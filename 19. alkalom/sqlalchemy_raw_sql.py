from sqlalchemy import create_engine

# database driver
# 3 féleképpen lehet használni
# 1. létrehozol egy adatbázis engine-t -> 

# 1 haszálati mód: natív sql

engine = create_engine('sqlite:///movies.db', echo=False)

sql_statement = """
        create table if not exists movies (
            title text,
            director text,
            release_date date
        )
"""

insert_statement = """
        insert into movies (title, director, release_date) 
            values 
        ('Doctor Strange 2', 'Sam Raimi', 2022)
"""

engine.execute(sql_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)
engine.execute(insert_statement)


select_statement = """
    select oid, t.* from movies t
"""

result_set = engine.execute(select_statement)

print(list(result_set))

for item in result_set:
    print(item)

engine.execute("alter table movies add row_num int")
engine.execute("update movies set row_num = oid")


engine.execute("delete from movies where 10 > row_num")