def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k] = L[i]
                i += 1
            elif L[i][1] == R[j][1] and L[i][0] < R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def greedy(ar, k, n):
    k = 0
    cnt = 1

    for m in range(1, n):
        if ar[m][0] >= ar[k][1]:
            cnt += 1
            k = m

    return cnt
        
n = int(input())
arr = []

for i in range(n):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    arr.append(tmp)


mergeSort(arr)
a = greedy(arr, 0, n)
print(a)

