#!/usr/bin/env python3

from brain_games.game import run_game
from brain_games.games.gcd import DESCRIPTION, get_puzzle


def main():
    run_game(DESCRIPTION, get_puzzle)


if __name__ == '__main__':
    main()
