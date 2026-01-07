import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    DP = [[0] * 16]
    DP[0][0b0000] = 1
    DP[0][0b1100] = 1
    DP[0][0b0110] = 1
    DP[0][0b0011] = 1
    DP[0][0b1111] = 1

    while True:
        next_count = [0] * 16
        
        '''
        가로 블록을 가장 우선적으로 넣고,
        세로 블록을 넣을 수 있는 경우를 확인.

        가로 블록은 이전 칸을 메꿀 수 있는 유일한 블록으로,
        이전 칸의 파인 곳의 모든 부분에 넣어야만 함.

        세로 블록을 넣을 수 있는 경우는
        1. 앞 칸이 전부 채워졌거나
        2. 현재 칸의 연속된 두 칸이 비어있거나
        '''

        for i in range(16):
            next_count[i ^ 15] += DP[-1][i]

        next_count[0b1111] += next_count[0b0000]
        next_count[0b1111] += next_count[0b1100]
        next_count[0b1111] += next_count[0b1001]
        next_count[0b1111] += next_count[0b0011]

        next_count[0b1100] += next_count[0b0000]
        next_count[0b0110] += next_count[0b0000]
        next_count[0b0011] += next_count[0b0000]

        if next_count[15] >= 2_147_483_647:
            break
        else:
            DP.append(next_count)

    N = int(next(iterator))
    for _ in range(N):
        print(DP[int(next(iterator))-1][-1])


if __name__ == "__main__":
    solve()