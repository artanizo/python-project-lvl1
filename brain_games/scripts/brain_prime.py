#!/usr/bin/env python3

from brain_games.games.prime import description, get_puzzle
from brain_games.game import game


def main():
    game(description, get_puzzle)


if __name__ == '__main__':
    main()
