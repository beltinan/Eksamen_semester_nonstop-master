from CustomerRepository import CustomerRepository

# Contract Sender
class ContractSender:
    def __init__(self, customer_repository, database_connector):
        self.customer_repository = customer_repository
        self.database_connector = database_connector

    def send_contract(self, customer_id, contract_content):
        customer = self.customer_repository.get_customer_by_id(customer_id)
        if customer is None:
            print("Customer not found!")
            return

        self.customer_repository.add_contract(customer_id, contract_content)
        print("Contract sent successfully to customer", customer.name)
