import numpy as np
from time import time
from random import random


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(t2 - t1)
        return result

    return wrap_func


shape = 128
pole = [[[0] for i in range(shape)] for j in range(shape)]
nPole = np.array([[0] * shape] * shape)


def gen_fields(size, chance):
    for row in range(size):
        for column in range(size):
            if random() < chance:
                pole[row][column] = 1
                nPole[row][column] = 1
            else:
                pole[row][column] = 0
                nPole[row][column] = 0


def near(x, y, size, field):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if field[i - (abs(i) // size) * size][j - (abs(j) // size) * size]:
                count += 1
    return count


gen_fields(shape, 0.5)


@timer_func
def game(field, iter):
    alive = 0
    size = len(field)
    for i in range(iter):
        for row in range(size):
            for column in range(size):
                if field[row][column] == 0 and near(row, column, size, field) == 3:
                    field[row][column] = 1
                elif field[row][column] == 1 and near(row, column, size, field) != 3\
                        and near(row, column, size, field) != 4:
                    field[row][column] = 0

    for row in range(size):
        for column in range(size):
            if field[row][column] == 1:
                alive += 1

    print(alive)


game(pole, 128)
game(nPole, 128)
