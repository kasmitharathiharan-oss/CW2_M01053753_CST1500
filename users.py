import bcrypt
import pandas as pd

def add_user(conn, name, hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?,?)"
    parram = (name,hash_password)
    curr.execute(sql,parram)
    conn.commit()

def migrate_users(conn):
    with open("DATA/user.txt","r") as f:
        users = f.readlines()

    for user in users:
        name, hash = user.strip().split(",")
        add_user(conn, name, hash)
    conn.close()

def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * from users"
    curr.execute(sql)
    users = curr.fetchall() # all user table as list
    conn.close()
    return(users)

def get_user(conn, name_):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = (name_,)
    curr.execute(sql,param)
    user = curr.fetchone()
    return user
