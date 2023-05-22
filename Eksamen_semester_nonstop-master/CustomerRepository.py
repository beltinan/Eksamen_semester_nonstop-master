from Customer import Customer
from Contract import Contract
class CustomerRepository:
    def __init__(self, database_connector):
        self.database_connector = database_connector
        self.customers = self.get_customers()

    def get_customers(self):
        customers = []
        customer_query = f"SELECT name, email, cvr, id FROM Customer"
        self.database_connector.cursor.execute(customer_query)
        customer_data = self.database_connector.cursor.fetchall()
        for customer_tuple in customer_data:
            contracts = []
            contract_query = f'''
            SELECT Contract.customer_id, Contract.content, Contract.status, Contract.id
            FROM Customer LEFT JOIN Contract on customer.id = contract.customer_id
            WHERE customer.id = {customer_tuple[-1]}'''
            self.database_connector.cursor.execute(contract_query)
            contract_data = self.database_connector.cursor.fetchall()
            if contract_data:
                for contract_tuple in contract_data:
                    contracts.append(Contract(*contract_tuple))
            customer = Customer(*customer_tuple, contracts)
            customers.append(customer)
        return customers

    def add_customer(self, name, email, cvr):
        query = f'''
        INSERT INTO Customer (name, email, cvr)
        VALUES ( '{name}', '{email}', {cvr});'''
        self.database_connector.cursor.execute(query)
        self.database_connector.connection.commit()
        customer = Customer(name, email, cvr, len(self.customers))
        self.customers.append(customer)
        print("Kunde tilføjet")

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def add_contract(self, customer_id, contract_content):
        contract = Contract(customer_id, contract_content)
        query = f"INSERT INTO Contract (customer_id, content, status) VALUES ({customer_id}, '{contract_content}', 'draft')"
        self.database_connector.cursor.execute(query)
        self.database_connector.connection.commit()
        self.customers[customer_id - 1].contracts.append(contract)
