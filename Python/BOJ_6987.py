import sys

def solve():
    read = sys.stdin.buffer.readline
    T = 4
    answer_list = [0] * 4

    for tc in range(T):
        result_list = list(map(int, read().split()))
        teams = []

        for i in range(6):
            teams.append(result_list[i * 3: (i + 1) * 3])

        flag = True
        for team in teams:
            if sum(team) != 5:
                flag = False
        
        if not flag:
            continue

        comb_list = []
        battle_list = [(0, 2), (1, 1), (2, 0)]
        for i in range(6):
            for j in range(i + 1, 6):
                comb_list.append((i, j))
        

        def DFS(index):
            nonlocal tc

            if index >= len(comb_list):
                answer_list[tc] = 1
                return
            
            if answer_list[tc]:
                return

            a, b = comb_list[index]
            for battle in range(3):
                i, j = battle_list[battle]

                if teams[a][i] and teams[b][j]:
                    teams[a][i] -= 1
                    teams[b][j] -= 1

                    DFS(index + 1)

                    teams[a][i] += 1
                    teams[b][j] += 1

        DFS(0)

    print(*answer_list)


if __name__ == "__main__":
    solve()