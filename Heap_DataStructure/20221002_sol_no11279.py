import sys

def max_heapify(index):
    
    l = 2 * index + 1
    r = 2 * index + 2
    largest = index

    if l <= len(ar) - 1:
        if ar[l] > ar[index]:
            largest = l

    if r <= len(ar) - 1:
        if ar[r] > ar[largest]:
            largest = r

    if largest != index:
        tmp = ar[index]
        ar[index] = ar[largest]
        ar[largest] = tmp

        max_heapify(largest)

def heap_increase_key(index, key):
    if key < ar[index]:
        return

    ar[index] = key

    while index > 0 and ar[(index - 1) // 2] < ar[index]:
        tmp = ar[(index - 1) // 2]
        ar[(index -  1) // 2] = ar[index]
        ar[index] = tmp
        index = (index - 1) // 2

n = int(sys.stdin.readline())
length = 0
ar = [0] * n

for i in range(n):
    val = int(sys.stdin.readline())
    
    if val == 0:
        print(ar[0])
        
        if length > 0:
            length -= 1
            
        if ar[0] != 0:            
            ar[0] = ar[length]
            ar[length] = 0
            max_heapify(0)

            
    else:
        heap_increase_key(length, val)
        length += 1

