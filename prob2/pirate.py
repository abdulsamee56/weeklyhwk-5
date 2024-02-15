import random

class PiratePlunder:
    def __init__(self, initial_bank):
        self.treasure_chest = self.build_treasure_chest()
        self.bank = initial_bank

    def build_treasure_chest(self):
        """
        Build and populate the treasure chest with pirate-themed items.
        Returns a dictionary representing the treasure chest.
        """
        treasure_chest = {
            'Gold Doubloons': 50,
            'Precious Jewels': 20,
            'Black Pearls': 5,
            'Silver Pieces of Eight': 100,
            'Ancient Maps': 2
        }
        return treasure_chest

    def plunder_treasure_chest(self, wager):
        """
        Simulate plundering the pirate treasure chest and deduct the wager from the bank.
        Returns the result of the plunder (randomly selected item), the updated bank balance,
        and a message describing any additional events (e.g., risky events, regular loss, or bonus treasures).
        """
        if wager > self.bank:
            return "Insufficient funds", self.bank, ""

        self.bank -= wager

        # Introduce a regular unsuccessful event: 10% chance of losing a portion of the wager
        regular_loss_event = random.random() < 0.1
        if regular_loss_event:
            regular_loss = int(0.2 * wager)
            self.bank -= regular_loss
            event_message = f"Unsuccessful plunder! You lost ${regular_loss}."
        else:
            event_message = ""

        # Plunder the pirate treasure chest
        result = random.choice(list(self.treasure_chest.keys()))

        # Introduce a risky event: 30% chance of losing half of the wager
        risky_event = random.random() < 0.3
        if risky_event:
            loss = int(0.5 * wager)
            self.bank -= loss
            event_message += f"Risky event! You lost ${loss}."
        else:
            # Introduce a bonus event: 10% chance of finding extra treasure
            bonus_event = random.random() < 0.1
            if bonus_event:
                bonus = int(0.3 * wager)
                self.bank += bonus
                event_message += f"Bonus treasure! You found ${bonus} extra."

            # Update the bank based on the result
            if result == 'Gold Doubloons':
                self.bank += 10 * wager
            elif result == 'Precious Jewels':
                self.bank += 5 * wager
            elif result == 'Black Pearls':
                self.bank += 20 * wager
            elif result == 'Silver Pieces of Eight':
                self.bank += 8 * wager
            elif result == 'Ancient Maps':
                self.bank += 50 * wager

        return result, self.bank, event_message

# Example usage:
initial_bank_amount = 1000
pirate_game = PiratePlunder(initial_bank_amount)

while pirate_game.bank > 0:
    print(f"\nCurrent Pirate Booty: ${pirate_game.bank}")
    wager = int(input("Enter your wager (0 to quit): "))
    
    if wager == 0:
        print("Thanks for plundering! Exiting Pirate Plunder.")
        break

    result, updated_booty, event_message = pirate_game.plunder_treasure_chest(wager)
    print(f"Result of the plunder: {result}")
    print(f"Updated Pirate Booty: ${updated_booty}")
    if event_message:
        print(event_message)

    if updated_booty <= 0:
        print("Arrr! Ye be out of funds. Pirate Plunder be over!")
        break
