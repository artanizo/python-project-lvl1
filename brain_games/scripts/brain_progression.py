#!/usr/bin/env python3

from brain_games.game import game
from brain_games.games.progression import description, get_puzzle


def main():
    game(description, get_puzzle)


if __name__ == '__main__':
    main()
