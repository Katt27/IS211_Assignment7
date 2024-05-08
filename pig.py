import random

random.seed(0)  # Ensure reproducible rolls

class Die:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def __str__(self):
        return f"{self.name} has {self.total_score} points"

class PigGame:
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.die = Die()

    def play_turn(self, player):
        turn_points = 0
        print(f"\n{player.name}'s turn:")
        
        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}")
            if roll == 1:
                print("SCRATCH!!! No points for you this turn.")
                break
            turn_points += roll
            print(f"Current turn points: {turn_points} - Total possible score: {player.total_score + turn_points}")
            choice = input("Roll(r) or Hold(h)? ").strip().lower()
            if choice == 'h':
                player.total_score += turn_points
                break

    def play_game(self):
        print("Welcome to Pig!")
        while all(player.total_score < 100 for player in self.players):
            for current_player in self.players:
                self.play_turn(current_player)
                if current_player.total_score >= 100:
                    print(f"\n{current_player.name} wins with {current_player.total_score} points!")
                    return

if __name__ == "__main__":
    game = PigGame(["Player A", "Player B"])
    game.play_game()
