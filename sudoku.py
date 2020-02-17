#!/usr/bin/python

from termcolor import colored
import timeit
SIZE = 9
all_items = []


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

    all = set(range(1, 10))

    def __init__(self, index, xs, ys):
        self.index = index
        self.items = []
        self.xs = xs
        self.ys = ys

    def add(self, item):
        self.items.append(item)

    def fill(self, zero, val):
        for i in self.items:
            if i.x==zero.x and i.y == zero.y :
                i.val = val
                break
        for i in all_items:
            if i.x==zero.x and i.y == zero.y :
                i.val = val
                break
 

    def do_stuff(self):
        global all_items
        existing = set(x.val for x in self.items if x.val != 0)
        missing =  self.all - existing
        sols = {}
        zeros = [x for x in self.items if x.val == 0]

        for im in missing:
            checks = [x for x in all_items if x.val == im]

            for z in zeros:
                confirmed = 0
                for c in checks:
                    if c.x == z.x:
                        break
                    if c.y == z.y:
                        break
                    confirmed = confirmed +1
                    if confirmed == len(checks):
                        #print(c.val, "[",z.x,",", z.y,"]")
                        if c.val not in sols:
                            sols[c.val] = [z]
                        else:
                            sols[c.val].append(z)

        solve = []

        for k,v in sols.items():
            if len(v) == 1:
                self.fill(v[0],k)
            else:
                solve.append(k)

        return len(solve) == 0


if __name__ == "__main__":
    idxx = 0
    xs = []
    ys = []

    boxes = {}

    for x in range(SIZE):
        for y in range(SIZE):
            if x in [0, 1, 2] and y in [0, 1, 2]:
                idx = 1
                xs = [0, 1, 2]
                ys = [0, 1, 2]
            elif x in [3, 4, 5] and y in [0, 1, 2]:
                idx = 2
                xs = [3, 4, 5]
                ys = [0, 1, 2]
            elif x in [6, 7, 8] and y in [0, 1, 2]:
                idx = 3
                xs = [6, 7, 8]
                ys = [0, 1, 2]
            elif x in [0, 1, 2] and y in [3, 4, 5]:
                idx = 4
                xs = [0, 1, 2]
                ys = [3, 4, 5]
            elif x in [3, 4, 5] and y in [3, 4, 5]:
                idx = 5
                xs = [3, 4, 5]
                ys = [3, 4, 5]
            elif x in [6, 7, 8] and y in [3, 4, 5]:
                idx = 6
                xs = [6, 7, 8]
                ys = [3, 4, 5]
            elif x in [0, 1, 2] and y in [6, 7, 8]:
                idx = 7
                xs = [0, 1, 2]
                ys = [6, 7, 8]
            elif x in [3, 4, 5] and y in [6, 7, 8]:
                idx = 8
                xs = [3, 4, 5]
                ys = [6, 7, 8]
            elif x in [6, 7, 8] and y in [6, 7, 8]:
                idx = 9
                xs = [6, 7, 8]
                ys = [6, 7, 8]

            if idx not in boxes:
                boxes[idx] = Box(idx, xs, ys)

            m = M(Matrix[x][y], x, y)
            m.box = idx
            all_items.append(m)
            boxes[idx].add(m)

    def my_func():
        while True:
            count = 0
            for box in boxes.values():
                done = box.do_stuff()

                if done:
                    count = count+1
            if count == len(boxes):
                break

    print(timeit.timeit(my_func, number=1))

    print(25 * "=", end='')
    print()

    for m in all_items:
        print(m.to_color(), " ", end='')
        if m.y == 8:
            print()
