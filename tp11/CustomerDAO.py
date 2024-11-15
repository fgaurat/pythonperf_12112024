import sqlite3
from Customer import Customer


class CustomerDAO:

    def __init__(self, db_file):
        self.__con = sqlite3.connect(db_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            self.__con.commit()
        else:
            self.__con.rollback()
        self.__con.close()
        self.__con = None

    def find_all_old(self):
        the_list = []
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)
        for row in rs:
            c = Customer(*row)
            the_list.append(c)
        return the_list

    def find_all(self):
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)
        for row in rs:
            customer_data = {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "gender": row[4],
                "ip_address": row[5]
            }
            c = Customer(**customer_data)
            yield c

    def __del__(self):
        if self.__con:
            self.__con.close()
