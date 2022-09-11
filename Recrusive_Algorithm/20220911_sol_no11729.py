global cnt, A
cnt = 0
A = []
B = []

def hanoi(n):
    rHanoi(n, 1, 2, 3)
    return

def rHanoi(n, start, aux, to):
    global cnt, A, B
    cnt += 1
    
    if n == 1:
        A.append(start)
        B.append(to)
        return
    rHanoi(n-1, start, to, aux)
    A.append(start)
    B.append(to)
    rHanoi(n-1, aux, start , to)
    
    return

n = int(input())
hanoi(n)

print(cnt)
for i in range(len(A)):
    print("%d %d"%(A[i], B[i]))
