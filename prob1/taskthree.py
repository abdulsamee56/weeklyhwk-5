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
                'salesperson': fake.name(),
                'state': fake.state()  # Add state information for searching
            }

            # Store the generated user record with the user ID as the key
            self.data_warehouse[user_id] = user_record

    def display_data_warehouse(self):
        # Display the generated user records in the data warehouse with key-value pairs
        for user_id, user_record in self.data_warehouse.items():
            print(f"User ID: {user_id}, User Record: {user_record}")

    def search_by_state(self, target_state):
        # Search for users based on the specified state
        matching_users = {user_id: user_record for user_id, user_record in self.data_warehouse.items() if user_record.get('state') == target_state}
        return matching_users

    def search_by_salesperson(self, target_salesperson):
        # Search for users based on the specified salesperson
        matching_users = {user_id: user_record for user_id, user_record in self.data_warehouse.items() if user_record.get('salesperson') == target_salesperson}
        return matching_users

    def search_by_user_id(self, target_user_id):
        # Search for a user based on the specified user ID
        user_record = self.data_warehouse.get(target_user_id)
        return {target_user_id: user_record} if user_record else {}

# Example usage:
data_collector = DataCollector()
data_collector.generate_sample_data(10)  # Generate 10 sample records
data_collector.display_data_warehouse()  # Display the generated data with key-value pairs

# Search for users in a certain state
state_search_result = data_collector.search_by_state('California')
print(f"\nUsers in California:\n{state_search_result}")

# Search for users handled by a certain salesperson
salesperson_search_result = data_collector.search_by_salesperson('John Doe')
print(f"\nUsers handled by John Doe:\n{salesperson_search_result}")

# Search for a user by ID
user_id_search_result = data_collector.search_by_user_id(3)
print(f"\nUser with ID 3:\n{user_id_search_result}")
