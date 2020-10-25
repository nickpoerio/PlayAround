#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:17:15 2020

@author: Nicola Poerio
"""


class Player():
    def __init__(self, symbol, name):
        self.my_cells = []
        self.symbol = symbol
        self.name = name

    def play(self, free_cells):
        while 1:
            move = input('Player {} next move (1-9):'.format(self.symbol))
            if move in free_cells:
                self.my_cells.append(move)
                break
            else:
                print('Invalid entry')
        return move
