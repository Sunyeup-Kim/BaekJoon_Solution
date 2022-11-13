# 힙 자료구조 맞춤 제작

class heap:
    
    def __init__ (self, n):
        self.length = 0
        self.ar = [None]
        
        return

    # --------------최대힙 메쏘드-------------------------

    def max_heapify(self, index):
        # O(logn)
        
        l = 2 * index
        r = 2 * index + 1
        largest = index

        if l <= self.length:
            if self.ar[l][1] > self.ar[index][1]:
                largest = l

        if r <= self.length:
            if self.ar[r][1] > self.ar[largest][1]:
                largest = r

        if largest != index:
            tmp = self.ar[index]
            self.ar[index] = self.ar[largest]
            self.ar[largest] = tmp

            self.max_heapify(largest)

    def heap_increase_key(self, index):
        # O(logn)
        
        while index > 1 and self.ar[index // 2][1] < self.ar[index][1]:
            tmp = self.ar[index // 2]
            self.ar[index // 2] = self.ar[index]
            self.ar[index] = tmp
            index = index // 2

    def heap_max_insert(self, key):
        # O(logn)
        
        self.length += 1
        self.ar.append(key)
        self.heap_increase_key(self.length)


    def heap_extract_max(self):
        # O(logn)

        if self.length < 1:
            return

        MAX = self.ar[1]
        self.ar[1] = self.ar[self.length]
        self.ar.pop()
        self.length -= 1

        self.max_heapify(1)


        return MAX


    # --------------최소힙 메쏘드-------------------------

    def min_heapify(self, index):
        # O(logn)
        
        l = 2 * index
        r = 2 * index + 1
        smallest = index

        if l <= self.length:
            if self.ar[l][1] < self.ar[index][1]:
                smallest = l

        if r <= self.length:
            if self.ar[r][1] < self.ar[smallest][1]:
                smallest = r

        if smallest != index:
            tmp = self.ar[index]
            self.ar[index] = self.ar[smallest]
            self.ar[smallest] = tmp

            self.min_heapify(smallest)

    def heap_decrease_key(self, index):
        # O(logn)
        
        while index > 1 and self.ar[index // 2][1] > self.ar[index][1]:
            tmp = self.ar[index // 2]
            self.ar[index // 2] = self.ar[index]
            self.ar[index] = tmp
            index = index // 2

    def heap_min_insert(self, key):
        # O(logn)
        
        self.length += 1
        self.ar.append(key)
        self.heap_decrease_key(self.length)


    def heap_extract_min(self):
        # O(logn)

        if self.length < 1:
            return

        MIN = self.ar[1]
        self.ar[1] = self.ar[self.length]
        self.ar.pop()
        self.length -= 1

        self.min_heapify(1)


        return MIN

# _______main code________

import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    Q_max = heap(n)
    Q_min = heap(n)
    inputs = [False] * (n + 1)

    for j in range(n):
        command, value = sys.stdin.readline().split()
        value = int(value)

        if command == 'I':
            Q_max.heap_max_insert((j, value))
            Q_min.heap_min_insert((j, value))

            inputs[j] = True
            
        else:            
            if value == 1:

                elem = Q_max.heap_extract_max()

                if elem != None:
                    
                    while not inputs[elem[0]]:
                        elem = Q_max.heap_extract_max()

                        if elem == None:
                            break

            else:
                
                elem = Q_min.heap_extract_min()

                if elem != None:
                    
                    while not inputs[elem[0]]:
                        elem = Q_min.heap_extract_min()

                        if elem == None:
                            break

            if elem != None:
                inputs[elem[0]] = False
            
                
    # 최종 출력할 최대값
    MAX = Q_max.heap_extract_max()


    if MAX != None:
        
        while not inputs[MAX[0]]:
            MAX = Q_max.heap_extract_max()

            if MAX == None:
                break

    if MAX != None:
        inputs[MAX[0]] = False
    

    # 최종 출력할 최솟값
    MIN = Q_min.heap_extract_min()

        
    if MIN != None:
        
        while not inputs[MIN[0]]:
            MIN = Q_min.heap_extract_min()

            if MIN == None:
                break


    if MAX == None and MIN == None:
        print('EMPTY')
    elif MAX != None and MIN == None:
        print(MAX[1], MAX[1])
    else:
        print(MAX[1], MIN[1])
    
    del Q_max
    del Q_min
    
    
