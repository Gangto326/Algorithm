import sys
sys.setrecursionlimit(200_010)

def solution(k, room_number):
    parents = {}
    answer = []
    
    
    def find(index):
        if index in parents:
            parents[index] = find(parents[index])
            return parents[index]
        
        else:
            return index
        
    
    for room in room_number:
        if room in parents:
            i = find(parents[room])
            answer.append(i)
            parents[i] = i + 1
        
        else:
            answer.append(room)
            parents[room] = room + 1
    
    return answer