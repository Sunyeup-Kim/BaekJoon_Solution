# https://www.acmicpc.net/status?user_id=paul5506&problem_id=1074&from_mine=1

# what I learn
#- Recursion dont have to everything.
#ex. To get element at (7, 3), I dont have to start from (0, 0) to (7, 3) counting from 0

global num, r, c


def recursion(n, x, y):
    global num

    # base case

    if n == 0:
        return

    # recursion case
    else:
        n2 = n // 2
        x2 = x - n2
        y2 = y - n2
        
        if r < x2 and c < y2:
            recursion(n2, x - n2, y - n2)  #좌측상단 재귀

        elif r < x2 and c >= y2:
            num += n2 ** 2
            recursion(n2, x - n2, y)  #우측상단 재귀

        elif r >= x2 and c < y2:
            num += n2 ** 2 * 2
            recursion(n2, x, y - n2)  #좌측하단 재귀
            
        else:
            num += n2 ** 2 * 3
            recursion(n2, x, y)  #우측하단 재귀

        

        


N, r, c = map(int, input().split())
num = 0

recursion(2**N, 2**N, 2**N)
print(num)

