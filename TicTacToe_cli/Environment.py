#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:37:32 2020

@author: Nicola Poerio
"""


class Environment():
    def __init__(self):
        self.maze = [[], [], []]
        self.free_cells = []
        k = 1
        for i in range(0, 3):
            for j in range(0, 3):
                entry = str(k)
                self.maze[i].append(entry)
                self.free_cells.append(entry)
                k += 1

    def print(self):
        for i in range(0, 3):
            print(self.maze[i])

    def __getitem__(self, key):
        k = int(key) - 1
        i = k // 3
        j = k % 3
        return self.maze[i][j]

    def __setitem__(self, key, value):
        k = int(key) - 1
        i = k // 3
        j = k % 3
        self.maze[i][j] = value
        self.free_cells.remove(key)
