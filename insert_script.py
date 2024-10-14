from sqlalchemy import create_engine, insert, text
import time

time.sleep(5)

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()

query = text("INSERT INTO identify (_name, surname) VALUES ('Swift', 'John')")

conn.execute(query)
conn.commit()
print("OK")