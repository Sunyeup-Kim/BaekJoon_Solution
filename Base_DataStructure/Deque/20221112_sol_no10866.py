# question url: https://www.acmicpc.net/problem/10866

# 필요한 사전 작업

class Deque:

    def __init__(self):
        self.ar = []
    
    def push_front(self, x):
        self.ar.insert(0, x)

        return

    def push_back(self, x):
        self.ar.append(x)

        return

    def pop_front(self):

        if len(self.ar) == 0:
            return print(-1)

        val = self.ar[0]
        del self.ar[0]

        print(val)

        return

    def pop_back(self):

        if len(self.ar) == 0:
            return print(-1)

        val = self.ar.pop()

        print(val)

        return

    def size(self):
        print(len(self.ar))
        return

    def empty(self):

        if len(self.ar) == 0:
            return print(1)
        else:
            return print(0)


    def front(self):

        if len(self.ar) == 0:
            return print(-1)

        return print(self.ar[0])

    def back(self):

        if len(self.ar) == 0:
            return print(-1)

        return print(self.ar[len(self.ar) - 1])


# main
import sys

n = int(sys.stdin.readline())
deque = Deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deque.push_front(command[1])

    elif command[0] == 'push_back':
        deque.push_back(command[1])

    elif command[0] == 'pop_front':
        deque.pop_front()

    elif command[0] == 'pop_back':
        deque.pop_back()

    elif command[0] == 'size':
        deque.size()

    elif command[0] == 'empty':
        deque.empty()

    elif command[0] == 'front':
        deque.front()
        
    else:
        deque.back()


