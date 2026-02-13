# Tic-Tac-Toe

A simple command-line implementation of the classic Tic-Tac-Toe game written in Python.

## Description

This project is a text-based version of Tic-Tac-Toe where two players can play against each other on a 3x3 grid. The game alternates between Player 1 (X) and Player 2 (O) until one player wins or the game ends in a draw.

## Features

*   **Two-Player Mode:** Play against a friend on the same computer.
*   **Interactive CLI:** Simple command-line interface for inputting moves.
*   **Win Detection:** Automatically detects wins across rows, columns, and diagonals.
*   **Draw Detection:** Ends the game when the board is full and no winner is found.

## How to Run

1.  Make sure you have Python installed on your system.
2.  Navigate to the project directory:
    ```bash
    cd "tic-tac-toe"
    ```
3.  Run the game:
    ```bash
    python main.py
    ```

## Usage

1.  The game board is a 3x3 grid.
2.  Players take turns entering their moves.
3.  To make a move, enter the row and column numbers separated by a comma (e.g., `1,2` for Row 1, Column 2).
    *   Rows and columns are **1-indexed** (1, 2, or 3).
4.  The game announces the winner or if it ends in a draw.

## Requirements

*   Python 3.x
