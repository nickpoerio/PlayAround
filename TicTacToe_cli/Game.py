#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:48:23 2020

@author: Nicola Poerio
"""
from TicTacToe_cli.Player import Player
from TicTacToe_cli import ComputerPlayer
from TicTacToe_cli.Environment import Environment

import random


class Game():
    def __init__(self, nplayers):
        self.players = []
        if nplayers == 0:
            self.players.append(ComputerPlayer('O'))
            self.players.append(ComputerPlayer('X'))
        elif nplayers == 1:
            name = input('player O name:')
            self.players.append(Player('O', name))
            self.players.append(ComputerPlayer('X'))
        elif nplayers == 2:
            name1 = input('player O name:')
            self.players.append(Player('O', name1))
            name2 = input('player X name:')
            self.players.append(Player('X', name2))
        else:
            print('invalid number of players')
            return
        self.env = Environment()
        self.id = random.randint(0, 1)
        self.isEnd = False
        self.nmoves = 0
        self.max_moves = 9
        self.winner = []

    def play(self):
        # play
        player = self.players[self.id]
        while True:
            self.env.print()
            move = player.play(self.env.free_cells)
            self.env[move] = player.symbol
            self.nmoves += 1
            self._check_end(move, player.symbol)
            if self.isEnd is True:
                break
            self.id = (self.id+1) % 2
            player = self.players[self.id]

    def load_stats(self):
        self.load = []

    def save_stats(self):
        self.save = []

    def _check_end(self, move, symbol):
        for i in range(0, 3):
            if (self.env.maze[i].count(symbol) == 3 or
                    [self.env.maze[x][i] for x in range(0, 3)].count(symbol) == 3):
                self.isEnd = True
                self.winner = symbol
                self.env.print()
                print('The winner is {}'.format(symbol))
                return
        d1 = [self.env.maze[x][x] for x in range(0, 3)]
        d2 = [self.env.maze[x][2-x] for x in range(0, 3)]
        if (d1.count(symbol) == 3 or d2.count(symbol) == 3):
            self.isEnd = True
            self.winner = symbol
            self.env.print()
            print('The winner is {}'.format(symbol))
            return
        if self.nmoves == self.max_moves:
            self.isEnd = True
            self.env.print()
            print('No winner. End of game.')
            return
