#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rock Paper Scissor Game
"""

import random

COMPUTER_SCORE = 0
PLAYER_SCORE = 0
choices = ("rock", "paper", "scissor")


def get_player_choice():
    """Prompts the player to choose from three available options"""
    player_choice = input("rock, paper, or scissor: ")
    if player_choice in choices:
        return player_choice
    return get_player_choice()


def get_computer_choice():
    """Return the computer's choice"""
    return random.choice(choices)


def game():
    """Main Game Function"""
    player_answer = get_player_choice()
    computer_answer = get_computer_choice()
    print("your choice is: ", player_answer)
    print("the computer choice is: ", computer_answer)
    global COMPUTER_SCORE, PLAYER_SCORE
    if player_answer == computer_answer:
        print("no one wins, shoot!")
    # player wins
    if (
        (player_answer == "rock" and computer_answer == "scissor")
        or (player_answer == "scissor" and computer_answer == "paper")
        or (player_answer == "paper" and computer_answer == "rock")
    ):
        print(
            "you win!",
        )
        PLAYER_SCORE += 1
    # computer wins
    else:
        print("the computer wins!")
        COMPUTER_SCORE += 1


def result():
    """Displaying the result of the game."""
    print("player score: ", PLAYER_SCORE)
    print("computer score: ", COMPUTER_SCORE)

def play_game():
    """This function initiates a game consisting of four rounds"""
    for i in range(1, 4):
        print(f"Round Number {i}")
        game()
    result()


if __name__ == "__main__":
    print("welcome to the rock paper scissor game!!! ✂️")
    while True:
        play_game()
        another_game = int(
            input(
                "1 if you want to continue\n" +
                "2 if you want to reset and continue\n" +
                "3 if you want to quit\n"
            )
        )
        if another_game == 1:
            continue
        if another_game == 2:
            PLAYER_SCORE = 0
            COMPUTER_SCORE = 0
            continue
        print("Ok! Bye")
        break
