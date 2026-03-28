import sys
sys.setrecursionlimit(2000)

def solve():
    read = sys.stdin.readline
    N, M, K1, K2 = map(int, read().split())

    team1 = [[] for _ in range(N + 1)]
    team2 = [[] for _ in range(N + 1)]
    
    for _ in range(K1):
        i, j = map(int, read().split())
        team1[i].append(j)
        
    for _ in range(K2):
        i, j = map(int, read().split())
        team2[i].append(j)
        
    
    def DFS(index, visited, team, match_list):
        if not visited[index]:
            return False
        
        visited[index] = False

        for next_node in team[index]:
            if match_list[next_node] == 0 or DFS(match_list[next_node], visited, team, match_list):
                match_list[next_node] = index
                return True
            
        return False


    match_list = [0] * (M + 1)
    team1_count = 0
    for i in range(1, N + 1):
        visited = [True] * (N + 1)

        if DFS(i, visited, team1, match_list):
            team1_count += 1

    match_list = [0] * (M + 1)
    team2_count = 0
    for i in range(1, N + 1):
        visited = [True] * (N + 1)

        if DFS(i, visited, team2, match_list):
            team2_count += 1
    
    if team1_count < team2_count:
        print("네 다음 힐딱이")
    else:
        print("그만 알아보자")


if __name__ == "__main__":
    solve()