from CustomerDAO import CustomerDAO

def filter_male(stream):
    for customer in stream:
        if customer.gender == "Male":
            yield customer

def main():
    with CustomerDAO('customers_db.db') as dao:
        # customers = dao.find_all()
        male_customers = filter_male(dao.find_all())
        
        
        # print(next(customers))
        # print(next(customers))
        # print(next(customers))
        
        for customer in male_customers:
            print(customer)
        # for customer in customers:
        #     print(customer)
        # print(customers)
        # customers = list(customers)
        
        
    print('la fin')
if __name__=='__main__':
    main()
