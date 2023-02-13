# url of question: https://www.acmicpc.net/problem/1260

import sys

##Queue 구현
class Queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            return
        
        val = self.queue[0]
        del self.queue[0]

        return val

    def enqueue(self, element):
        val = self.queue.append(element)

    def printQueue(self):
        print(self.queue)



#BFS algorithm

def BFS(G, S):

    G[S][0] = 'Gray'
    print(S, end=' ')

    Q = Queue()
    Q.enqueue(S)

    while len(Q.queue) != 0:
        u = Q.dequeue()

        for v in G[u][1]:
            if G[v][0] == 'White':
                G[v][0] = 'Gray'
                Q.enqueue(v)
                print(v, end=' ')

        G[u][0] = 'Black'

    return


def DFS(G, S):

    
    if G[S][0] == 'White':
        print(S, end=' ')
        DFS_visit(G, S)

def DFS_visit(G, u):

    G[u][0] = 'Gray'

    for edge in G[u][1]:
        if G[edge][0] == 'White':
            print(edge, end=' ')
            DFS_visit(G, edge)

    G[u][0] = 'Black'
    
        

# 딕셔너리를 이용하여 인접리스트 형태의 그래프 자료구조를 구현한다
G = {}

V, E, S = map(int, sys.stdin.readline().split())

# 인접리스트 형태의 그래프 자료구조 형성
for i in range(1, V + 1):
    G[i] = ['White', []]

# 데이터 입력
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())

    # 무방향 그래프
    G[a][1].append(b)
    G[b][1].append(a)

for key in G:
    G[key][1].sort()

DFS(G, S)
print()

# 그래프 초기화
for i in range(1, V + 1):
    G[i][0] = 'White'

BFS(G, S)

