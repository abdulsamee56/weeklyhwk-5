# Import the Faker library, which allows me to generate fake data
from faker import Faker

class DataCollector:
    def __init__(self):
        # Initialize an empty list to store generated user records
        self.data_warehouse = []

    def generate_sample_data(self, num_records):
        # Create an instance of the Faker class
        fake = Faker()

        # Generate sample data for the specified number of records
        for _ in range(num_records):
            # Create a dictionary representing a user record with fake data
            user_record = {
                'username': fake.user_name(),
                'password': fake.password(),
                'birthdate': fake.date_of_birth().strftime('%Y-%m-%d'),
                'address': fake.address(),
                'social_security_number': fake.ssn(),
                'product_purchased': fake.random_element(elements=('ProductA', 'ProductB', 'ProductC')),
                'salesperson': fake.name()
            }

            # Append the generated user record to the data warehouse
            self.data_warehouse.append(user_record)

    def display_data_warehouse(self):
        # Display the generated user records in the data warehouse
        for record in self.data_warehouse:
            print(record)

# Example usage
data_collector = DataCollector()
data_collector.generate_sample_data(10)  # Generate 10 sample records
data_collector.display_data_warehouse()  # Display the generated data
