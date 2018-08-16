#!/usr/bin/env python3
"""
app.py

Rock, Paper, Scissors +
"""
import argparse
import os
import platform
from collections import namedtuple
from random import choice

from .models import Player, Roll, Sprite, plays

PLAYS = list(plays().keys())
OS = platform.system()

Params = namedtuple("Params", "rounds gui")


class Game:
    def __init__(self, player, rounds=3, gui=False):
        self.player = player
        self.pc = Player("computer")
        self.rounds = rounds
        self.gui = gui

    def end_game(self):
        winner = self.player if self.player.score > self.pc.score else self.pc
        clear_console()
        print()
        print("".center(72, "="))
        print(f"{winner} won the game!".center(72))
        print(
            f"{self.player}({self.player.score}) vs {self.pc}({self.pc.score})".center(
                72
            )
        )
        print("".center(72, "="))
        print()

    @staticmethod
    def get_player_roll(player):
        clear_console()
        print()
        for i, play in enumerate(PLAYS, 1):
            print(f"[{i:>2}] {play.title()}")
        while True:
            try:
                print()
                roll = int(input(f"\nWhich play do you choose {player}? ")) - 1
                return Roll(PLAYS[roll])
            except (IndexError, ValueError):
                print(f"You must enter a number between 1-{len(PLAYS)}")

    def run(self):
        count = 0
        try:
            while count < self.rounds:
                pc_roll = Roll(choice(PLAYS))
                player_roll = self.get_player_roll(self.player)

                if player_roll.name == pc_roll.name:
                    self.show_results(player_roll, pc_roll)
                    print("The game was a draw!")
                    pause()
                else:
                    outcome = player_roll.can_defeat(pc_roll)

                    result = self.player if outcome else self.pc
                    loser = "player" if result.name != self.player.name else "pc"
                    self.player.won() if outcome else self.pc.won()
                    count += 1

                    self.show_results(player_roll, pc_roll, loser=loser)
                    print(f"{result} won the match!")
                    pause()
            self.end_game()
        except KeyboardInterrupt:
            clear_console()
            print(f"Later {self.player}")

    def show_results(self, player_roll, pc_roll, loser=None):
        clear_console()
        if self.gui:
            _ = Sprite(player_roll, pc_roll, loser=loser)
        print()
        print("".center(72, "="))
        print()
        print(f"{self.player}[{player_roll}] vs {self.pc}[{pc_roll}]".center(72))
        print()
        print("".center(72, "="))
        print()


def clear_console():
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def get_args():
    """Argument parser."""
    parser = argparse.ArgumentParser(description="Rock, Paper, Scissor's +")
    parser.add_argument(
        "-r", "--rounds", type=int, help="How many rounds to play", required=False
    )
    parser.add_argument(
        "-g",
        "--gui",
        action="store_const",
        default=False,
        const=True,
        help="Display images",
    )
    args = parser.parse_args()
    rounds = args.rounds
    gui = args.gui
    params = Params(rounds=rounds, gui=gui)
    return params


def get_player_name():
    return input("What is your name? ")


def main():
    if platform.system() != "Linux":
        print(f"Sorry, your platform '{platform.system()}' is not supported!")
        exit(1)

    params = get_args()
    clear_console()
    print_header()

    rounds = params.rounds if params.rounds else 3
    gui = params.gui if params.gui else False

    try:
        rounds = int(rounds)
        name = get_player_name()
        player = Player(name)
        game = Game(player, rounds=rounds, gui=gui)
        game.run()
    except KeyboardInterrupt:
        clear_console()
        print("Game aborted!")
    except ValueError:
        print(f'"{rounds}" is not a valid value for rounds, must be a number!')


def pause():
    _ = input("\nHit ENTER to continue ")
    return None


def print_header():
    clear_console()
    print("".center(72, "="))
    print("Rock, Paper, Scissors, + 12 More!".center(72))
    print("".center(72, "="))
    print()


if __name__ == "__main__":
    main()
