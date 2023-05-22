from ContractSender import ContractSender
from CustomerRepository import CustomerRepository
from DatabaseConnector import DatabaseConnector
from Customer import Customer

# Create database connector and connect to the database
database_connector = DatabaseConnector("localhost")
database_connector.connect()

# Create customer repository
customer_repository = CustomerRepository(database_connector)

# Create some customers
customer_repository.add_customer("John Doe", "john.doe@example.com", 123)
customer_repository.add_customer("Jane Smith", "jane.smith@example.com", 123)
customer_repository.add_customer("Firat Kurt", "firo@haymana.kr", 40032)

# Create contract sender
contract_sender = ContractSender(customer_repository, database_connector)

# Send a contract to a customer
contract_sender.send_contract(1, "Contract 1 content")

# Get the contracts for a customer
customer_contracts = customer_repository.get_customer_by_id(1).get_contracts()
print("Contracts for customer 1:")
for contract in customer_contracts:
    print("Contract ID:", contract.id)
    print("Content:", contract.content)
    print("Status:", contract.get_status())

# Close the database connection
database_connector.disconnect()

