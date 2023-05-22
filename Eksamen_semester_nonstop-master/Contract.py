# Contract
class Contract:
    def __init__(self, customer_id, content, status = "draft", id = None):
        self.id = id
        self.customer_id = customer_id
        self.content = content
        self.status = status

    def get_status(self):
        return self.status

    def sign(self):
        self.status = 'signed'