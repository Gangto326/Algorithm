import sys

def solve():
    read = sys.stdin.readline

    N = int(read())
    n_list = list(map(int, read().split()))

    M = int(read())
    m_list = list(map(int, read().split()))

    answer_list = [(-1, -1)]

    for target in range(100, -1, -1):
        n_start = answer_list[-1][0] + 1
        
        for i in range(n_start, N):
            if n_list[i] == target:
                m_start = answer_list[-1][1] + 1

                for j in range(m_start, M):
                    if m_list[j] == target:
                        answer_list.append((i, j))
                        break
    
    print(len(answer_list) - 1)
    for i in range(1, len(answer_list)):
        if i == len(answer_list) - 1:
            print(n_list[answer_list[i][0]])
        else:
            print(n_list[answer_list[i][0]], end = " ")
    

if __name__ == "__main__":
    solve()