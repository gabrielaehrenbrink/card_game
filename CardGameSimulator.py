import random

class GameSimulator:
    def __init__(self, num_simulations):
        self.num_simulations = num_simulations
        self.deck = [i for i in range(1, 14)] * 4 
        self.results = []

    def run_simulation(self):
        for _ in range(self.num_simulations):
            result = self.play_game()
            self.results.append(result)

    def play_game(self):
        random.shuffle(self.deck)
        positions = [None] * 13
        deck_index = 0

        while deck_index < len(self.deck):
            card = self.deck[deck_index]
            pos = random.randint(0, 12)

            if positions[pos] is None and (pos + 1) == card:
                positions[pos] = card
                deck_index = 0  
            else:
                deck_index += 1

            if None not in positions:
                break

        correct_positions = sum(1 for i, card in enumerate(positions) if card == i + 1)
        is_successful = correct_positions == 13
        return (is_successful, correct_positions)

    def calculate_statistics(self):
        total_games = len(self.results)
        successful_games = sum(1 for result in self.results if result[0])
        success_rate = (successful_games / total_games) * 100

        card_positions = [result[1] for result in self.results]
        avg_correct_positions = sum(card_positions) / total_games

        return {
            'total_games': total_games,
            'successful_games': successful_games,
            'success_rate': success_rate,
            'avg_correct_positions': avg_correct_positions
        }

    def percentage_for_correct_positions(self, num_correct_positions):
        total_games = len(self.results)
        games_with_correct_positions = sum(1 for result in self.results if result[1] == num_correct_positions)
        return (games_with_correct_positions / total_games) * 100


# Example of using the GameSimulator
if __name__ == "__main__":
    num_simulations = 100000  # Number of simulations to run
    simulator = GameSimulator(num_simulations)
    simulator.run_simulation()
    stats = simulator.calculate_statistics()
    
    print("Total Games:", stats['total_games'])
    print("Successful Games:", stats['successful_games'])
    print("Success Rate:", stats['success_rate'], "%")
    print("Average Correct Positions:", stats['avg_correct_positions'])
    
    # Example to get percentage for a specific number of correct positions
    num_correct_positions = 12
    percentage = simulator.percentage_for_correct_positions(num_correct_positions)
    print(f"Percentage of games with exactly {num_correct_positions} correct positions: {percentage} %")
