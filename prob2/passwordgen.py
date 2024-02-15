import random
import string
import matplotlib.pyplot as plt

class PasswordSimulatorWithVisualization:
    def __init__(self):
        self.accepted_passwords = set()
        self.unaccepted_passwords = set()
        self.dictionary_words = self.load_dictionary_words()

    def load_dictionary_words(self):
        return ['password', '123456', 'qwerty', 'secret', 'letmein', 'admin', 'welcome', 'monkey', '12345']

    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def is_acceptable_password(self, password):
        has_special_symbol = any(char in string.punctuation for char in password)
        not_in_dictionary = password.lower() not in self.dictionary_words
        return has_special_symbol and not_in_dictionary

    def simulate_password_generation(self, iterations=40):
        iteration_numbers = list(range(1, iterations + 1))
        accepted_counts = []
        unaccepted_counts = []

        for i in range(iterations):
            password = self.generate_random_password()

            if self.is_acceptable_password(password):
                print(f"Iteration {i + 1}: Acceptable Password - {password}")
                self.accepted_passwords.add(password)
            else:
                print(f"Iteration {i + 1}: Unacceptable Password - {password}")
                self.unaccepted_passwords.add(password)

            accepted_counts.append(len(self.accepted_passwords))
            unaccepted_counts.append(len(self.unaccepted_passwords))

        # Visualization
        plt.bar(iteration_numbers, accepted_counts, label='Accepted Passwords', color='green')
        plt.bar(iteration_numbers, unaccepted_counts, label='Unaccepted Passwords', color='red', alpha=0.5)
        plt.xlabel('Iterations')
        plt.ylabel('Number of Passwords')
        plt.title('Password Acceptance Over Iterations')
        plt.legend()
        plt.show()

# Example usage:
password_simulator_with_visualization = PasswordSimulatorWithVisualization()
password_simulator_with_visualization.simulate_password_generation()
