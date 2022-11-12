# https://www.acmicpc.net/status?user_id=paul5506&problem_id=1436&from_mine=1

n = int(input())

cnt = 0
num = 665

while cnt != n:

    num += 1
    tmp = num
    six_count = 0

    while tmp != 0:
        if tmp % 10 == 6:
            six_count += 1
        else:
            six_count = 0

        if six_count == 3:
            cnt += 1
            break

        tmp //= 10


print(num)
