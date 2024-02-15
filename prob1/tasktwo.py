from faker import Faker

class DataCollector:
    def __init__(self):
        # Initialize an empty dictionary to store user records with unique IDs as keys
        self.data_warehouse = {}

    def generate_sample_data(self, num_records):
        # Create an instance of the Faker class
        fake = Faker()

        # Generate sample data for the specified number of records
        for user_id in range(1, num_records + 1):
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

            # Store the generated user record with the user ID as the key
            self.data_warehouse[user_id] = user_record

    def display_data_warehouse(self):
        # Display the generated user records in the data warehouse with key-value pairs
        for user_id, user_record in self.data_warehouse.items():
            print(f"User ID: {user_id}, User Record: {user_record}")

# Example usage:
data_collector = DataCollector()
data_collector.generate_sample_data(10)  # Generate 10 sample records
data_collector.display_data_warehouse()  # Display the generated data with key-value pairs
