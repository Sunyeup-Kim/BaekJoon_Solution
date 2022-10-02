def Dynamic_Programming(k, n):

    # base case
    if n == 1:
       ar[k][n] = 1
       return 
    
    # recursion case
    if ar[k][n - 1] == 0:
        Dynamic_Programming(k, n - 1)
    if ar[k - 1][n] == 0:
        Dynamic_Programming(k - 1, n)
        
    ar[k][n] = ar[k][n - 1] + ar[k - 1][n]   
    

n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())

    ar = [[1 * j for j in range(n+1)]]
    # '얕은 복사'와 '깊은 복사' 유의하기!!
    ar.extend([[0] * (n + 1) for j in range(k)])

    Dynamic_Programming(k, n)
    print(ar[k][n])
