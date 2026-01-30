import sys

def solve():
    read = sys.stdin.readline
    T = list(read().rstrip('\n'))
    P = list(read().rstrip('\n'))
    answer = []


    def get_pi(pattern):
        size = len(pattern)
        DP = [0] * size
        j = 0

        for i in range(1, size):
            while j and pattern[i] != pattern[j]:
                j = DP[j-1]
            
            if pattern[i] == pattern[j]:
                j += 1
                DP[i] = j

        return DP
    

    def kmp(string, pattern):
        table = get_pi(pattern)
        string_size = len(string)
        pattern_size = len(pattern) - 1
        j = 0

        for i in range(string_size):
            while j and string[i] != pattern[j]:
                j = table[j-1]

            if string[i] == pattern[j]:
                if j == pattern_size:
                    answer.append(i - pattern_size + 1)
                    j = table[j]

                else:
                    j += 1


    kmp(T, P)
    print(len(answer))
    print(*answer)


if __name__ == "__main__":
    solve()