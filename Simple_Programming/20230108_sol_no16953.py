# https://www.acmicpc.net/problem/16953

a, b = map(int, input().split())


num = 1

while a != b and a < b:


    if b % 2 == 0:

        num += 1
        b //= 2

    elif b % 10 == 1:
        num += 1
        b //= 10

    else:
        num = -1
        break


if a != b:
    num = -1


print(num)
