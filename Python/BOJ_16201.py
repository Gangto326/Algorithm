import sys
from collections import defaultdict

def solve():
    MOD = 1_000_000_007
    read = sys.stdin.readline
    R, C, K = map(int, read().split())

    block_dict = defaultdict(list)
    for _ in range(K):
        row, col = map(int, read().split())
        block_dict[row].append(col)

    total_tiles = 0
    answer = 1
    for row in block_dict:
        col_list = sorted(block_dict[row])
        col_list.append(C+1)

        start_index = 0
        for col in col_list:
            length = col - start_index - 1
            tile_count = length // 2

            if length % 2 != 0:
                answer = (answer * (tile_count + 1)) % MOD
            
            total_tiles += tile_count
            start_index = col
    
    no_block = R - len(block_dict)

    if no_block > 0:
        tile_count = C // 2

        if C % 2 != 0:
            answer = (answer * pow((tile_count + 1), no_block, MOD)) % MOD
        total_tiles += tile_count * no_block

    print(total_tiles, answer)


if __name__ == "__main__":
    solve()