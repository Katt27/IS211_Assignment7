import random

class Die:
    """Represents a single six-sided die."""
    def roll(self):
        """Returns a random roll between 1 and 6."""
        return random.randint(1, 6)

class Player:
    """Represents a player in the Pig game."""
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def __str__(self):
        """String representation of the player's current score."""
        return f"{self.name} has {self.total_score} points"

class PigGame:
    """Manages the Pig game logic."""
    def __init__(self):
        self.players = [Player("AAAAA"), Player("BBBBB")]
        self.die = Die()

    def play_turn(self, player):
        """Plays a single turn for the specified player."""
        turn_points = 0
        rolling = True

        while rolling:
            roll = self.die.roll()
            if roll == 1:
                print(f"It's {player.name} turn...\n{player.name} rolled a one. SCRATCH!!! No points for you.")
                turn_points = 0
                rolling = False
            else:
                turn_points += roll
                print(f"{player.name} rolled a {roll}\n{player.name} has {turn_points} points so far - Possible Points {player.total_score + turn_points}")
                choice = input("Roll(r) or Hold(h)? ").lower()
                rolling = choice == 'r'
                if not rolling:
                    player.total_score += turn_points

        print(player)
        print("--------------------------------------------------------")

    def play_game(self):
        """Plays the game until one of the players reaches 100 points."""
        print("Welcome to Pig!")
        player_index = 0

        while all(player.total_score < 100 for player in self.players):
            current_player = self.players[player_index]
            self.play_turn(current_player)
            player_index = (player_index + 1) % len(self.players)
        
        winner = max(self.players, key=lambda p: p.total_score)
        print(f"{winner.name} wins with {winner.total_score} points!")

if __name__ == "__main__":
    game = PigGame()
    game.play_game()
