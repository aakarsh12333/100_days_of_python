<img width="1405" height="768" alt="Gemini_Generated_Image_hfoq9shfoq9shfoq" src="https://github.com/user-attachments/assets/c5d05917-2909-423f-9d56-83d897dde1dd" />


# Hangman Game

A simple Python Hangman game built as part of the 100 Days of Python practice.

## Overview

This project contains a console-based Hangman game where the player guesses letters to discover a hidden word. The game tracks wrong guesses and draws a simple hangman figure as the player makes mistakes.

## How to run

1. Open the project folder in your terminal.
2. Run the game with:

```bash
git init
python hangman_game.py
```

> Note: You only need `git init` if the repository is not already initialized.

## Game rules

- Enter a single letter as a guess.
- The game shows the current word progress with underscores for unknown letters.
- You have 5 incorrect guesses before the game ends.
- After the game ends, you can choose to play again.

## Files

- `hangman_game.py` - main Python script for the Hangman game.
- `.gitignore` - ignores `__pycache__/` and `.pyc` files.

## Notes

- Make sure you run the script with Python 3.
- Do not enter more than one character when guessing.
