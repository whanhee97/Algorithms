# 백준 10845 - 큐

import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.insert(0, cmd[1])
        ##print(queue)

    elif cmd[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
# import sys
# input = sys.stdin.readline

# class Queue:
#     def __init__(self):
#         self.arr = []

#     def push(self,x):
#         self.arr.append(x)
    
#     def pop(self):
#         if len(self.arr)==0:
#             return -1
#         return self.arr.pop(0)
    
#     def size(self):
#         return len(self.arr)

#     def empty(self):
#         if len(self.arr) == 0:
#             return 1
#         else:
#             return 0
#     def front(self):
#         if len(self.arr)==0:
#             return -1
#         return self.arr[0]
#     def back(self):
#         if len(self.arr)==0:
#             return -1
#         return self.arr[-1]

# n = int(input())
# q = Queue()
# for _ in range(n):
#     cmd = input().split()
#     if cmd[0] == 'push':
#         print(q.push(cmd[1]))
#     elif cmd[0] == 'pop':
#         print(q.pop())
#     elif cmd[0] == 'size':
#         print(q.size())
#     elif cmd[0] == 'empty':
#         print(q.empty())
#     elif cmd[0] == 'front':
#         print(q.front())
#     elif cmd[0] == 'back':
#         print(q.back())
