# Customer
class Customer:
    def __init__(self, name, email, cvr, id=None, contracts = []):
        self.id = id
        self.name = name
        self.email = email
        self.cvr = cvr
        self.contracts = contracts

    def add_contract(self, contract):
        self.contracts.append(contract)

    def get_contracts(self):
        return self.contracts