import sys

def solve():
    read = sys.stdin.readline
    S, T = read().rstrip(), read().rstrip()


    def DFS(string, S):
        if len(string) == len(S):
            if string == S:
                return 1
            else:
                return 0
            
        if string[-1] == 'A':
            if DFS(string[:-1], S):
                return 1
        
        if string[0] == 'B':
            if DFS(string[1:][::-1], S):
                return 1

        return 0
    

    print(DFS(T, S))


if __name__ == "__main__":
    solve()