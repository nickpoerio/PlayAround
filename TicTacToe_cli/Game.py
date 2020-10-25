#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:48:23 2020

@author: Nicola Poerio
"""
from TicTacToe_cli import Player, ComputerPlayer, Environment

import random


class Game():
    def __init__(self, nplayers):
        if nplayers == 0:
            self.player[0] = ComputerPlayer('O')
            self.player[1] = ComputerPlayer('X')
        elif nplayers == 1:
            name = input('player O name:')
            self.player[0] = Player('O', name)
            self.player[1] = ComputerPlayer('X')
        elif nplayers == 2:
            name1 = input('player O name:')
            self.player[0] = Player('O', name1)
            name2 = input('player X name:')
            self.player[1] = Player('X', name2)
        else:
            print('invalid number of players')
            return
        self.table = Environment()
        self.idx = random.randint(0, 2)
        self.isEnd = False

    def play(self):
        # play
        while True:
            self.player[self.idx].play()
            self._player_idx()
            self.player[self.idx].play()
            self._player_idx()
            self._check_end()
            if self.isEnd is True:
                break

    def load_stats(self):
        self.load = []

    def save_stats(self):
        self.load = []

    def _player_idx(self):
        self.idx = (self.idx+1) % 2

    def _check_end(self):
        self.check = []
        return False
