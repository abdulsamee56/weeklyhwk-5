from faker import Faker
import random

class ProductPurchasedDataCollector:
    def __init__(self):
        # Initialize the Faker instance for generating fake data
        self.fake = Faker()
        # Initialize an empty list to store generated user data
        self.data = []

    def generate_user_data(self, num_entries):
        """
        Generate user data and populate the 'data' list with dictionaries containing
        information such as username, web order, product ID, quantity, date of order, and region.
        """
        for _ in range(num_entries):
            user_data = {
                'Username': self.fake.user_name(),
                'WebOrder': self.fake.uuid4(),
                'ProductID': f'ID-{self.fake.uuid4()}',
                'Quantity': random.randint(1, 10),
                'DateOfOrder': self.fake.date(),
                'Region': self.fake.random_element(elements=('North', 'South', 'East', 'West'))
            }
            # Append the generated user data dictionary to the 'data' list
            self.data.append(user_data)

    def search_data(self, key, value):
        """
        Search for entries in the 'data' list with a specific key/value pair.
        Returns a list of matching entries.
        """
        results = [entry for entry in self.data if entry.get(key) == value]
        return results

# Example usage:
data_collector = ProductPurchasedDataCollector()
# Generate 10 entries of user data
data_collector.generate_user_data(10)

# Print generated data
print("Generated Data:")
for entry in data_collector.data:
    print(entry)

# Search for entries with a specific key/value pair (Using regions, North, South, East, West)
search_results = data_collector.search_data('Region', 'South')
print('\nSearch Results for Region="South":')
for result in search_results:
    print(result)
