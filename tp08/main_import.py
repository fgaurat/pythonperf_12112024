from csv import DictReader
import sqlite3
def main():
    data_file = "MOCK_DATA.csv"
    sql ="INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES(?,?,?,?,?)"
    con = sqlite3.connect("customers_db.db")
    with open(data_file) as f:
        data = DictReader(f)
        for d in data:
            del d['id']
            print(d)
            con.execute(sql,list(d.values()))
            
    con.commit()
    con.close()
if __name__=='__main__':
    main()
