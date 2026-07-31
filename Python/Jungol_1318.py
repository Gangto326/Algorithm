import sys

def solve():
    ugly = [0] * 1501
    ugly[1] = 1
    
    p2 = 1
    p3 = 1
    p5 = 1
    
    for i in range(2, 1501):
        next_val = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
        ugly[i] = next_val
        
        if next_val == ugly[p2] * 2:
            p2 += 1
        if next_val == ugly[p3] * 3:
            p3 += 1
        if next_val == ugly[p5] * 5:
            p5 += 1

    input_data = sys.stdin.read().split()
    iterator = iter(input_data)
    
    answer = []
    while True:
        query = int(next(iterator))
        
        if query == 0:
            break
            
        answer.append(str(ugly[query]))
        
    print('\n'.join(answer))
    

if __name__ == "__main__":
    solve()