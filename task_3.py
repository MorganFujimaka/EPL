#!/usr/bin/python

import sys


def visit(row_num, col_num):
    matrix = [[0 for _ in range(col_num)] for _ in range(row_num)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = c = di = 0

    for i in range(row_num * col_num):
        print(r, c)

        matrix[r][c] = 1
        cr = r + dr[di]
        cc = c + dc[di]

        if 0 <= cr < row_num and 0 <= cc < col_num and matrix[cr][cc] is 0:
            r = cr
            c = cc
        else:
            di = (di + 1) % 4
            r = r + dr[di]
            c = c + dc[di]


if __name__ == "__main__":
    row_num = int(sys.argv[1])
    col_num = int(sys.argv[2])

    visit(row_num, col_num)
