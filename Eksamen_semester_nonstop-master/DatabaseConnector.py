from MySQLdb import connect, Error
import Customer
import ContractSender
import Contract
import CustomerRepository


class DatabaseConnector:
    def __init__(self, database_url):
        self.database_url = database_url

    def connect(self):
        try:
            self.connection = connect(
                host='localhost',
                user='root',
                database='nonstopcontracts',
                password='1Din2Far3'
            )
            self.cursor = self.connection.cursor()
            print("Forbindelse til databasen oprettet.")
        except Error as error:
            print(f"Fejl under oprettelse af forbindelse til databasen: {error}")

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("Forbindelse til databasen lukket.")

#
# # Opret en instans af DatabaseConnector
# database_connector = DatabaseConnector("localhost")
#
# # Opret forbindelse til databasen
# database_connector.connect()
#
# # Hent kundeoplysninger fra databasen
# customer_id = 1
# customer = database_connector.fetch_customer(customer_id)
#
# if customer:
#     print("Kunde fundet:")
#     print("ID:", customer.id)
#     print("Navn:", customer.name)
#     print("E-mail:", customer.email)
#     print("CVR:", customer.cvr)
# else:
#     print("Kunde ikke fundet.")
#
# # Luk forbindelsen til databasen
# database_connector.disconnect()
