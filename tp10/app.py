from flask import Flask,render_template
from CustomerDAO import CustomerDAO


app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/moche')
def index_moche():
    html = ""
    with CustomerDAO(r"..\customers_db.db") as dao:
        customers = dao.find_all()
        for customer in customers:
            html+=f"<li>{customer.first_name} {customer.last_name}</li>"
    return f"<ul>{html}</ul>"    

@app.route('/')
def index():
    with CustomerDAO(r"..\customers_db.db") as dao:
        customers = list(dao.find_all())
    return render_template('customers.html',customers = customers)

@app.route('/api/customers')
def get_customers():
    with CustomerDAO(r"..\customers_db.db") as dao:
        customers = list(dao.find_all())
    return customers