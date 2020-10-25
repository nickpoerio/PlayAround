# -*- coding: utf-8 -*-
"""
PlayAround games

Authors: Nicola Poerio & Leonardo Poerio
Date: 18th October 2020

"""
import argparse


def main(arguments):
    print('Init')
    if arguments.game == "TicTacToe_cli":
        from TicTacToe_cli.Game import Game
        game = Game(arguments.nplayers)
        game.play()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PlayAround argument parser')
    parser.add_argument('--game', type=str, help='Insert game name', default='TicTacToe_cli')
    parser.add_argument('--nplayers', type=int, help='number of players: 0-2', default=2)
    args = parser.parse_args()
    main(args)
