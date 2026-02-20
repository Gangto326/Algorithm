import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    num_list = list(map(int, read().split()))

    minus_list = []
    add_list = []

    for num in num_list:
        if num > 0:
            add_list.append(num)
        else:
            minus_list.append(num)
    
    minus_list.sort(reverse = True)
    add_list.sort()

    answer_list = []
    while minus_list or add_list:
        if minus_list:
            answer_list.append(abs(minus_list[-1]))

            for _ in range(M):
                minus_list.pop()

                if not minus_list:
                    break
        
        if add_list:
            answer_list.append(add_list[-1])

            for _ in range(M):
                add_list.pop()

                if not add_list:
                    break
    
    answer_list.sort()
    answer = answer_list[-1]
    for i in range(len(answer_list)-1):
        answer += answer_list[i] * 2
    
    print(answer)
    

if __name__ == "__main__":
    solve()