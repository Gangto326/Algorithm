import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    dna_list = [read().rstrip() for _ in range(N)]
    answer = 50


    def permutation(count, check, perm):
        nonlocal N, dna_list, answer

        if count >= N:
            total = len(perm[-1])

            for i in range(1, N):
                last_dna = perm[i-1][-1]

                flag = False
                for j in range(len(perm[i]) - 1, -1, -1):
                    if (perm[i][j] == last_dna) and (perm[i-1][-j - 1:] == perm[i][:j + 1]):
                        total += len(perm[i-1]) - (j + 1)
                        flag = True
                        break
                
                if not flag:
                    total += len(perm[i-1])
            
            answer = min(answer, total)
                    

        for i in range(N):
            if check[i]:
                check[i] = False
                perm.append(dna_list[i])

                permutation(count + 1, check, perm)

                check[i] = True
                perm.pop()


    permutation(0, [True] * N, [])
    print(answer)


if __name__ == "__main__":
    solve()