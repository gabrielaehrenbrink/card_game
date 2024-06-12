# Card Game Simulator

## Overview

This project is a Python-based simulation of a card game. The goal of the game is to place cards in the correct positions based on their value. The game uses a standard 52-card deck, and the simulation calculates the success rate and other statistics based on multiple game iterations.

## Game Rules

1. The game uses a standard deck of 52 cards, with four sets of cards ranging from 1 to 13.
2. The cards are placed one at a time in a position from 1 to 13.
3. If a card is placed in the position that matches its value (e.g., a card with value 1 in position 1), it stays there.
4. If a card does not match the position, it is returned to the deck.
5. The game continues until all cards are correctly placed or the deck runs out of cards.
6. A game is considered successful if all positions (1 to 13) have the correct cards.

## Features

- Simulate multiple games to gather statistics.
- Calculate the percentage of successful games.
- Determine the average number of correct card positions per game.
- Calculate the percentage of games with a specific number of correct card positions.