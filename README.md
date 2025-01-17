# Tic-Tac-Toe Coding Exercise: Terminal Edition

## Table of Contents:
1. [Objective](#objective)
2. [Lesson Requirements](#lesson-requirements)
3. [Key Concepts](#key-concepts)
4. [Stretch Goals](#stretch-goals)
5. [Developer Integrity](#developer-integrity)
6. [How to run](#how-to-run)

<a name="objective"></a>
## Objective
Create a simple tic-tac-toe game in Python that can be played in the terminal against a computer opponent.

<a name="lesson-requirements"></a>
## Lesson Requirements
1. Setup and Basics
   - Create a Python script file (e.g., tic_tac_toe.py).
   - Define a 3x3 grid to represent the tic-tac-toe board. Use a 2D list or a single list.
   - Write a function to display the board to the terminal.
2. Core Game Logic
   - Write a function to allow a player to make a move.
   - Write a function to allow the computer to make a move using a basic strategy.
3. Game Mechanics
   - Define a function to check for a winner (rows, columns, diagonals).
   - Define a function to check for a tie (all cells filled with no winner).
   - Alternate turns between the player and the computer.
4. Player Input and Validation
   - Use input() to get player moves.
   - Ensure the program handles invalid input gracefully.
5. Enhancements (Optional)
   - Allow the player to choose their symbol (X or O).
   - Let the player decide if they want to go first or second.
   - Add a basic AI strategy for the computer.

<a name="key-concepts"></a>
## Key Concepts You Will Learn
- Basic Python syntax: Variables, lists, functions, and loops.
- Input handling: Reading and validating user input.
- Logic implementation: Conditions and flow control with if statements.
- Randomization: Using the random module for computer moves.
- Code structure: Organizing functions for clarity and reusability.

<a name="stretch-goals"></a>
## Stretch Goals (Advanced Concepts, Optional)
- Implement a smarter AI using the Minimax algorithm.
- Add colors to the terminal output using libraries like colorama.
- Create a replay option for the game.

<a name="developer-integrity"></a>
## Developer Integrity:
- AI is a last resort and will not be used to create code.
  - It can be used to explain concepts or possibly help finding a function/module, but using other resources should come first. Example resources:
    - [W3 Schools](https://www.w3schools.com/python/default.asp)
    - [Official Python documentation](https://docs.python.org/3/)
    - Search engines (Google, DuckDuckGo, etc.)
  - Some helpful places to start:
    - [Data Types](https://www.w3schools.com/python/python_datatypes.asp)
    - [Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
    - [Python Functions](https://docs.python.org/3/library/functions.html)
- Never use code that you don't understand or can't explain.
  - It's real easy to use code found somewhere like StackOverflow, but this doesn't help build the skills we're trying to build. 
- Any approach is fine, as long as it is written in Python and works as intended.
- Ask questions.
  - Reach out to your peers and mentors if you need help.

<a name="how-to-run"></a>
## How to run:
1. Clone the repository using `git clone` 
   - [Instructions on GitHub](https://github.com/git-guides/git-clone)
2. Open a terminal session in the location that the repository was cloned and run `run_game.py` via Python 
   - (e.g. `python run_game.py`)
