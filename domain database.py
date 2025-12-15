import sqlite3
import pandas as pd
from pathlib import Path

DATA_DIR = Path("DATA")
path = DATA_DIR / "intelligence_platform.db"

def create_user_table(conn):
    curr = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS users ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    username TEXT NOT NULL UNIQUE, 
                    password_hash TEXT NOT NULL); """
    curr.execute(sql)
    conn.commit()

# C - Create   Add new data                    INSERT - user
def add_user(conn, name, hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?,?)"
    parram = (name,hash_password)
    curr.execute(sql,parram)
    conn.commit()


def migrate_users():
    with open("DATA/user.txt","r") as f:
        users = f.readlines()

    for user in users:
        name, hash = user.strip().split(",")
        add_user(conn, name, hash)
    conn.close()

# R - Read    Retrieve data              SELECT - user
def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * from users"
    curr.execute(sql)
    users = curr.fetchall() # all user table as list
    conn.close
    return(user)


def get_user(name_):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = (name_,)
    curr.execute(sql,param)
    user = curr.fetchone()
    conn.close()
    return user

def migrate_dataset_metadata(conn):
    data = pd.read_csv("DATA/datasets_metadata.csv")
    data.to_sql('datasets_metadata', conn, if_exists="append", index = False)
    conn.close()
 
def migrate_it_tickets(conn):
    data = pd.read_csv("DATA/it_tickets.csv")
    data.to_sql('it_tickets', conn)

def migrate_cyber_incidents(conn):
    data = pd.read_csv("DATA/cyber_incidents.csv")
    data.to_sql('cyber_incidents', conn)

def get_all_users_pandas():
    sql = "SELECT * from datasets_metadata"
    data = pd.read_sql(sql, conn)
    return(data)

conn = sqlite3.connect('DATA/intelligence_platform.db')
migrate_cyber_incidents(conn)
migrate_it_tickets(conn)
conn.close()



'''
# INSERT, UPDATE, and DELETE operations
conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()
sql = ""
parr = ""
curr.execute(sql. parr)
conn.commit()
conn.close()

# GETTING DATA from table INSERTED from the connections 
conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()
sql = ""
parr = ""
curr.execute(sql. parr)
cur.fetchall() 
curr.fetchone()
conn.close()
                
'''
