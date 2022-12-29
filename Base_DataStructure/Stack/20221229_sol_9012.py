# Question URL: https://www.acmicpc.net/problem/9012

import sys

N = int(sys.stdin.readline())


for i in range(N):
    

    INPUT = input()
    x = []
    y = []

    for j in range(len(INPUT)):

        if INPUT[j] == '(':
            x.append(INPUT[j])
        else:
            y.append(INPUT[j])

        if len(x) < len(y):
            break

    if len(x) == len(y):
        print('YES')
    else:
        print('NO')
