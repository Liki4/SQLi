#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine, exc
from hashlib import sha256

engine = create_engine("mysql+pymysql://root:TjsDgwGPz5ANbJUU@127.0.0.1:5738/sqli", max_overflow=5)

def query(username, password):
    with engine.connect() as con:
        query_exec = f"SELECT password FROM users WHERE username = '{username}'"
        print(query_exec)
        try:
            if con.execute(query_exec).scalar():
                passhash = con.execute(query_exec).fetchone()[0]
                return passhash == sha256(password.encode()).hexdigest()
        except exc.SQLAlchemyError as e:
            print(str(e.__dict__['orig']))
        return False


def main():
    username = input("Give me your username: ")
    password = input("Give me your password: ")
    print("Login success" if query(username, password) else "Login failed")

if __name__ == "__main__":
    main()

