def binaryPreOrder(index):
    
    print(ar[index], end='')
    
    L = 2 * index + 1
    R = 2 * index + 2

    if L <= len(ar) - 1:
        if ar[L] != '.':
            binaryPreOrder(L)
    if R <= len(ar) - 1:
        if ar[R] != '.':
            binaryPreOrder(R)

def binaryPostOrder(index):
        
    L = 2 * index + 1
    R = 2 * index + 2

    if L <= len(ar) - 1:
        if ar[L] != '.':
            binaryPostOrder(L)
    if R <= len(ar) - 1:
        if ar[R] != '.':
            binaryPostOrder(R)

    print(ar[index], end='')

def inOrder(index):

    L = 2 * index + 1
    R = 2 * index + 2

    if L <= len(ar) - 1:
        if ar[L] != '.':
            inOrder(L)
            
    print(ar[index], end='')
            
    if R <= len(ar) - 1:
        if ar[R] != '.':
            inOrder(R)

n = int(input())
ar = ['.'] * n
ar[0] = 'A'

for i in range(n):
    node = input().split()
    num = ar.index(node[0])
    
    L = 2 * num + 1
    R = 2 * num + 2

    if R >= len(ar):
        ar.extend(['.']*num)

    if node[1] != '.':
        ar[L] = node[1]
    if node[2] != '.':
        ar[R] = node[2]


binaryPreOrder(0)
print()
inOrder(0)
print()
binaryPostOrder(0)

