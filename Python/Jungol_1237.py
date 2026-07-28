import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, list(read().strip()))) for _ in range(N)]


    def combination(index, li, total):
        nonlocal N, board

        if len(li) == total:
            flag = True

            for i in li:
                if not flag:
                    break

                for j in li:
                    if i == j:
                        continue

                    if board[i][j] != 1:
                        flag = False
                        break
            
            if flag:
                return 1
            else:
                return 0
        
        if index >= N:
            return 0
        
        count = 0
        for i in range(index, N):
            li.append(i)
            count += combination(i + 1, li, total)
            li.pop()

        return count


    answer = ""
    for i in range(1, N + 1):
        if i != N:
            answer += str(combination(0, [], i)) + ", "
        else:
            answer += str(combination(0, [], i))

    print(answer)


if __name__ == "__main__":
    solve()