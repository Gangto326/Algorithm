import sys
from collections import deque

sentence = deque(sys.stdin.readline().rstrip())

for i in range(1, len(sentence)):
    string_list = []

    for j in range(i):
        string_list.append(sentence.popleft())

    next_str = sentence.popleft()
    flag = string_list[0] >= next_str

    if not flag:
        sentence.appendleft(next_str)
    
    while string_list:
        sentence.appendleft(string_list.pop())
    
    if flag:
        sentence.appendleft(next_str)
        
print("".join(sentence))