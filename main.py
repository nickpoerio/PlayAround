# -*- coding: utf-8 -*-
"""
PlayAround games

Authors: Nicola Poerio & Leonardo Poerio
Date: 18th October 2020

"""
import argparse


def main(arguments):

    if arguments.game == "TicTacToe_cli":
        import TicTacToe_cli
        game = TicTacToe_cli.Game()

        # print("Game {} initialized".format(arguments.game))
        # print("Number of players: {}".format(arguments.nplayers))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PlayAround argument parser')
    parser.add_argument('--game', type=str, help='Insert game name', default='TicTaCToe_cli')
    parser.add_argument('--nplayers', type=int, help='number of players: 0-2', default=2)
    args = parser.parse_args()
    main(args)
