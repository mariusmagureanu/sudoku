#!/usr/bin/env python

from termcolor import colored
import timeit

all_items = {}
all = set(range(1, 10))

Matrix = [[3, 0, 0, 2, 4, 0, 0, 6, 0],
          [0, 4, 0, 0, 0, 0, 0, 5, 3],
          [1, 8, 9, 6, 3, 5, 4, 0, 0],
          [0, 0, 0, 0, 8, 0, 2, 0, 0],
          [0, 0, 7, 4, 9, 6, 8, 0, 1],
          [8, 9, 3, 1, 5, 0, 6, 0, 4],
          [0, 0, 1, 9, 2, 0, 5, 0, 0],
          [2, 0, 0, 3, 0, 0, 7, 4, 0],
          [9, 6, 0, 5, 0, 0, 3, 0, 2]]
'''
Matrix = [[0, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 4, 0, 6, 0, 0, 0, 0, 3],
          [0, 7, 4, 0, 8, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 3, 0, 0, 2],
          [0, 8, 0, 0, 4, 0, 0, 1, 0],
          [6, 0, 0, 5, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 7, 8, 0],
          [5, 0, 0, 0, 0, 9, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 4, 0]]
'''


class M:
    def __init__(self, value, x, y):
        self.val = value
        self.x = x
        self.y = y
        self.box = 0
        self.color = 'green'
        if x in [3, 4, 5] and y in [3, 4, 5]:
            self.color = 'green'
        elif x in [3, 4, 5] or y in [3, 4, 5]:
            self.color = 'red'

    def to_color(self):
        return colored(self.val, self.color)


class Box:

    def __init__(self, index):
        self.index = index
        self.items = {}

    def add(self, item):
        self.items[(item.x, item.y)] = item

    def fill(self, zero, val):
        t_z = zero
        t_z.val = val
        self.items[(zero.x, zero.y)] = t_z
        all_items[(zero.x, zero.y)] = t_z

    def solve(self):
        global all_items
        existing = set(x.val for x in self.items.values() if x.val != 0)
        missing = all - existing
        sols = {}
        zeros = [x for x in self.items.values() if x.val == 0]

        for im in missing:
            checks = [x for x in all_items.values() if x.val == im]
            for z in zeros:
                confirmed = 0
                for c in checks:
                    if c.x == z.x:
                        break
                    if c.y == z.y:
                        break

                    confirmed = confirmed + 1
                    if confirmed == len(checks):
                        if c.val not in sols:
                            sols[c.val] = [z]
                        else:
                            sols[c.val].append(z)

        done = len(sols)

        for k, v in sols.items():
            if len(v) == 1:
                self.fill(v[0], k)
                done = done - 1

        return done == 0


def get_boxes(grid):
    boxes = {}

    yc = 0
    xc = 1

    for j, arr in enumerate(grid):
        xc = 1

        for i, mv in enumerate(arr):
            idx = xc + 3 * yc
            if idx not in boxes:
                boxes[idx] = Box(idx)

            m = M(mv, i, j)
            m.box = idx

            all_items[(i, j)] = m
            boxes[idx].add(m)

            if (i + 1) % 3 == 0:
                xc = xc + 1

        if (j + 1) % 3 == 0:
            yc = yc + 1

    return boxes


def solve_grid(boxes):
    while True:
        count = 0
        for box in boxes.values():
            done = box.solve()
            if done:
                count = count + 1
        if count == len(boxes):
            break


def print_grid_items():
    print(25 * "=", end='')
    print()

    for m in all_items.values():
        print(m.to_color(), " ", end='')
        if m.x == 8:
            print()


if __name__ == "__main__":
    boxes = get_boxes(Matrix)

    print(
        timeit.timeit(
            'solve_grid(boxes)',
            setup="from __main__ import solve_grid, boxes",
            number=1))
    print_grid_items()
