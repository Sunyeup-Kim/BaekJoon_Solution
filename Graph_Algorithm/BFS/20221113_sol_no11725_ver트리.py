# Node 정의: https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8

class Node:
    
    def __init__(self, element):
        self.element = element
        self.parent = None
        self.children = None
        self.next = None

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



class Tree_structure:

    def __init__(self):
        self.L = Node(1) # 루트 정의


    def find_element(self, elem1, elem2):
        # 레벨 순회 알고리즘 활용

        Q = Queue()
        Q.enqueue(self.L)

        while ~Q.isEmpty():
            v = Q.dequeue()

            if v.element == elem1 or v.element == elem2:
                break

            child_node = v.children
            while child_node != None:
                
                Q.enqueue(child_node)
                child_node = child_node.next


        return v
        

    def push(self, a, b):

        node = self.find_element(a, b)

        if node.children != None:

            tmp = node.children

            while tmp.next != None:
                tmp = tmp.next

            if node.element == a:
                tmp.next = Node(b)
                tmp.next.parent = a

            else:
                tmp.next = Node(a)
                tmp.next.parent = b

        else:
            if node.element == a:
                node.children = Node(b)
                node.children.parent = a

            else:
                node.children = Node(a)
                node.children.parent = b
                
        

        return

    def find_parents(self, node):
        #선위 순회 활용

        self.result[node.element] = node.parent

        tmp = node.children
        while tmp != None:
            self.find_parents(tmp)
            tmp = tmp.next
        

    def print_parents(self, n):
        self.result = {}

        self.find_parents(self.L)

        for i in range(2, n + 1):
            print(self.result[i])


import sys

n = int(sys.stdin.readline())
tree = Tree_structure()

# 인접 연결 리스트 형태로 노드간의 연결형태 입력

for i in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())

    tree.push(x, y)

tree.print_parents(n)


