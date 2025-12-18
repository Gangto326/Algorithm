import sys
from collections import deque

read = sys.stdin.readline

str_list = deque(read().rstrip())
boom = read().rstrip()

stack = []
dump_stack = []
boom_count = len(boom)
index = 0

while str_list:    
    next_string = dump_stack.pop() if dump_stack else str_list.popleft()
    stack.append(next_string)

    if next_string == boom[index]:
        index += 1

        if index == boom_count:
            for _ in range(boom_count):
                stack.pop()
            for _ in range(boom_count-1):
                if stack:
                    dump_stack.append(stack.pop())
            index = 0
    else:
        index = 1 if next_string == boom[0] else 0

while dump_stack:
    stack.append(dump_stack.pop())

print("".join(stack) if stack else "FRULA")