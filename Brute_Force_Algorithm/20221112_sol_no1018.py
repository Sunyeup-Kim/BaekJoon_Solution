import sys

## 데이터 입력
x, y = map(int,sys.stdin.readline().split())
ar = []

for i in range(x):
    tmp = list(sys.stdin.readline())
    ar.append(tmp)


## brute force algorithm
cnt_min = 9999999

for i in range(x - 7):
    for j in range(y - 7):

        
        for color in range(2):
            if color == 0:
                rec = 'W'
            else:
                rec = 'B'

            cnt = 0
            
            for k in range(8):
                for l in range(8):

                    if rec != ar[i + k][j + l]:
                        cnt += 1

                    if rec == 'W':
                        rec = 'B'
                    else:
                        rec = 'W'

                if rec == 'W': # 다음 행의 첫번째 열의 값을 고
                    rec = 'B'
                else:
                    rec = 'W'

            if cnt_min > cnt:
                cnt_min = cnt


print(cnt_min)
            
