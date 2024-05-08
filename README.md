# IS211_Assignment7
IS211_Assignment7

# Pig Game

## Overview
This repository contains the implementation of the "Pig" game, a popular two-player dice game. The objective is for players to reach 100 points before their opponent. Players take turns rolling a die, accumulating points each turn, but risking losing them all if they roll a one.

## Rules of the Game
- Players take turns to roll a six-sided die.
- On each turn, a player repeatedly rolls the die until either:
  - A 1 is rolled: The turn ends with the player scoring zero points for that turn.
  - The player holds: The sum of the rolls is added to the player's total score.
- The first player to accumulate 100 or more points wins the game.

## How to Run the Game
To play the game, follow these steps:
1. Ensure you have Python installed on your computer.
2. Download the `pig_game.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `pig_game.py`.
5. Run the script by entering `python pig_game.py`.
6. Follow the on-screen prompts to play the game.

## Implementation Details
This project uses basic concepts of Object-Oriented Programming (OOP):
- **Die Class**: Represents a single six-sided die, responsible for generating random rolls.
- **Player Class**: Manages the state and score of individual players.
- **PigGame Class**: Handles the game logic, player turns, and determines the game outcome.

The game is implemented in Python and demonstrates the use of classes, loops, and user input handling.

## Features
- Interactive command-line interface for rolling the die and choosing when to hold.
- Automatic tracking of player scores and game state.
- Clear output of game progress and results.

## Future Enhancements
- Add support for more than two players.
- Implement a graphical user interface (GUI).
- Provide an option to set different score limits.

Thank you for checking out the Pig Game. Enjoy playing!
