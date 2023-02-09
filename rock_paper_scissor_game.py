#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:46:37 2023

@author: rajaalebchiri
"""

import random

computer_score = 0
player_score = 0
choices = ("rock", "paper", "scissor")


def get_player_choice():
    player_choice = input("rock, paper, or scissor: ")
    if player_choice in choices:
        return player_choice
    else:
        get_player_choice()


def get_computer_choice():
    return random.choice(choices)


def game():
    player_answer = get_player_choice()
    computer_answer = get_computer_choice()
    print("your choice is: ", player_answer)
    print("the computer choice is: ", computer_answer)
    global computer_score, player_score
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
        player_score += 1
    # computer wins
    else:
        print("the computer wins!")
        computer_score += 1


def result():
    print("player score: ", player_score)
    print("computer score: ", computer_score)


def play_game():
    for i in range(4):
        game()
    result()


if __name__ == "__main__":
    print("welcome to the rock paper scissor game!!! ✂️")
    while True:
        play_game()
        another_game = int(
            input(
                "1 if you want to continue\n2 if you want to reset and continue\n3 if you want to quit\n"
            )
        )
        if another_game == 1:
            continue
        elif another_game == 2:
            player_score = 0
            computer_score = 0
            continue
        else:
            print("Ok! Bye")
            break
