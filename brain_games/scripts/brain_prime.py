#!/usr/bin/env python3

from brain_games.games.prime import DESCRIPTION, get_puzzle
from brain_games.game import run_game


def main():
    run_game(DESCRIPTION, get_puzzle)


if __name__ == '__main__':
    main()
