# Question URL: https://www.acmicpc.net/problem/11725

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

    def isEmpty(self):
        
        if len(self.queue) == 0:
            return True

        else:
            return False


def BFS(G, ar):
    # BFS 알고리즘 활용

    G[1][0] = 'Gray'

    Q = Queue()
    Q.enqueue(1)

    while not Q.isEmpty():
        u = Q.dequeue()

        for v in G[u][1]:
            
            if G[v][0] == 'White':
                
                G[v][0] = 'Gray'                
                Q.enqueue(v)

                ar[v] = u

        G[u][0] = 'Black'

    return
        



# 딕셔너리를 이용하여 인접리스트 형태의 그래프 자료구조를 구현한다
import sys
G = {}

N = int(sys.stdin.readline())
ar = [0] * (N + 1)

# 인접리스트 형태의 그래프 자료구조 형성
for i in range(1, N + 1):
    G[i] = ['White', []]

# 데이터 입력
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())

    # 무방향 그래프
    G[a][1].append(b)
    G[b][1].append(a)


BFS(G, ar)

for i in range(2, len(ar)):
    print(ar[i])
