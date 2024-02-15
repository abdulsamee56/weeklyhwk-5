import random
class GameOfChance:
    def __init__(self, initial_bank):
        self.treasure_chest = self.build_treasure_chest()
        self.bank = initial_bank

    def build_treasure_chest(self):
        """
        Build and populate the treasure chest with items.
        Returns a dictionary representing the treasure chest.
        """
        treasure_chest = {
            'Gold Coins': 50,
            'Gems': 20,
            'Diamonds': 5,
            'Silver Coins': 100,
            'Artifacts': 2
        }
        return treasure_chest

    def spin_treasure_chest(self, wager):
        """
        Simulate spinning the treasure chest and deduct the wager from the bank.
        Returns the result of the spin (randomly selected item), the updated bank balance,
        and a message describing any additional events (e.g., loss of money).
        """
        if wager > self.bank:
            return "Insufficient funds", self.bank, ""

        self.bank -= wager

        # Spin the treasure chest
        result = random.choice(list(self.treasure_chest.keys()))

        # Introduce a risky event: 20% chance of losing half of the wager
        risky_event = random.random() < 0.2
        if risky_event:
            loss = int(0.5 * wager)
            self.bank -= loss
            event_message = f"Risky event! You lost ${loss}."
        else:
            event_message = ""

        # Update the bank based on the result
        if result == 'Gold Coins':
            self.bank += 10 * wager
        elif result == 'Gems':
            self.bank += 5 * wager
        elif result == 'Diamonds':
            self.bank += 20 * wager
        elif result == 'Silver Coins':
            self.bank += 8 * wager
        elif result == 'Artifacts':
            self.bank += 50 * wager

        return result, self.bank, event_message

# Example usage:
initial_bank_amount = 1000
game = GameOfChance(initial_bank_amount)

while game.bank > 0:
    print(f"\nCurrent Bank Balance: ${game.bank}")
    wager = int(input("Enter your wager (0 to quit): "))
    
    if wager == 0:
        print("Thanks for playing! Exiting the game.")
        break

    result, updated_bank, event_message = game.spin_treasure_chest(wager)
    print(f"Result of the spin: {result}")
    print(f"Updated Bank Balance: ${updated_bank}")
    if event_message:
        print(event_message)

    if updated_bank <= 0:
        print("Sorry, you're out of funds. Game over!")
        break
