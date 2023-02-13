# Question URL:https://www.acmicpc.net/status?user_id=paul5506&problem_id=11660&from_mine=1

import sys


# 필요한 자료구조 정의
global result
global ar

result = []
ar = []


N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    ar.append(list(map(int, sys.stdin.readline().split())))
    result.append([0] * N)


# 누적 합 구하기
for i in range(N):
    tmp = 0
    
    for j in range(N):
        tmp += ar[i][j]

        if i:
            result[i][j] = tmp + result[i-1][j]
        else:
            result[i][j] = tmp
        

# 알고리즘 시작

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # 행렬이 0으로 시작하기 때문에 변수 수정
    x1, y1 = x1 - 1, y1 - 1
    x2, y2 = x2 - 1, y2 - 1

                                          
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp

    tmp = result[x2][y2]

    if y1 - 1 >= 0:
        tmp -= result[x2][y1 - 1]

    if x1 - 1 >= 0:
        tmp -= result[x1 - 1][y2]

    if x1 - 1 >= 0 and y1 -1 >= 0:
        tmp += result[x1 - 1][y1 - 1]
    

    print(tmp)        
