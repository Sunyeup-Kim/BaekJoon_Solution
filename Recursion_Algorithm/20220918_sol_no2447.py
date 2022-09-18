# 이 문제는 결국 이해를 못해 다른 분의 코드를 익혔다

def paint_star(LEN):
    DIV3 = LEN//3
    if LEN == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*']*3
        return
    
    paint_star(DIV3)

    for i in range(0, LEN, DIV3):
        for j in range(0, LEN, DIV3):
            if i != DIV3 or j != DIV3:
                for k in range(DIV3):
                    g[i+k][j:j+DIV3] = g[k][:DIV3]

n = int(input())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()
#출처: https://cotak.tistory.com/38 [TaxFree:티스토리]
