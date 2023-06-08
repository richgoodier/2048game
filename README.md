# 2048 Game in Python using Pygame

This project implements a simple version of the game 2048 using Python and the Pygame library for the user interface.

## Getting Started

To run this code, make sure you have Python installed along with the Pygame library.

### Prerequisites

This code depends on Pygame. You can install Pygame from the provided `requirements.txt` file using pip:

```sh
pip install -r requirements.txt
```

## How to run the game

To run the game, execute the python script with a Python interpreter in your terminal:

```sh
python 2048game.py
```

## Game Instructions

Welcome to 2048. Use the arrow keys to play. The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048.

Here are the controls:
- Up Arrow: Shift tiles up
- Down Arrow: Shift tiles down
- Left Arrow: Shift tiles left
- Right Arrow: Shift tiles right

Each turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4. Tiles slide as far as possible in the chosen direction until they are stopped by another tile or the edge of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.

You win the game when you create a tile with the number 128, and you lose if there are no legal moves left.

## Built With

- Python 3
- Pygame

## Code Structure

This code is structured as follows:

- The main game loop is in the `play` method of the `Game2048` class. This loop continues running until the player wins or loses.
- The `listen_for_move` method captures user input.
- The `calculate_board` method calculates the new state of the board after each move.
- The `add_number_to_board` method adds a new number to the board.
- The `draw_board` method redraws the board on the screen.
- The `check_win_state` and `check_lose_state` methods check whether the game has been won or lost.
