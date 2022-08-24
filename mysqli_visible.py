#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine
from prettytable import from_db_cursor

engine = create_engine("mysql+pymysql://root:TjsDgwGPz5ANbJUU@127.0.0.1:5738/sqli", max_overflow=5)

def query(username):
    with engine.connect() as con:
        query_exec = f"SELECT * FROM users WHERE username = '{username}'"
        print(query_exec)
        cur = con.execute(query_exec).cursor
        x = from_db_cursor(cur)
        return(x)

def main():
    username = input("Give me your username: ")
    print(query(username))

if __name__ == "__main__":
    main()

