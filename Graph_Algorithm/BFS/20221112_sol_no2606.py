# url of question
# https://www.acmicpc.net/status?user_id=paul5506&problem_id=2606&from_mine=1

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

def BFS(G):

    G[1][0] = 'Gray'

    Q = Queue()
    Q.enqueue(1)

    while len(Q.queue) != 0:
        u = Q.dequeue()

        for v in G[u][1]:
            if G[v][0] == 'White':
                G[v][0] = 'Gray'
                Q.enqueue(v)

        G[u][0] = 'Black'

    return
    

# 딕셔너리를 이용하여 인접리스트 형태의 그래프 자료구조를 구현한다
G = {}

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

# 인접리스트 형태의 그래프 자료구조 형성
for i in range(1, V + 1):
    G[i] = ['White', []]

# 데이터 입력
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())

    # 무방향 그래프
    G[a][1].append(b)
    G[b][1].append(a)


BFS(G)

cnt = 0
for i in range(2, len(G) + 1):
    if G[i][0] != 'White':
        cnt += 1

print(cnt)
