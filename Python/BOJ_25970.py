import sys

def solve():
    read = sys.stdin.readline
    B = int(read())
    low_bit = [read().strip() for _ in range(B)]
    high_bit = [read().strip() for _ in range(B)]

    N = int(read())
    for _ in range(N):
        data = read().strip()

        low_count = 0
        high_count = 0
        for i in range(len(data)):
            for j in range(B):
                lb = low_bit[j]
                if len(lb) <= len(data) - i:
                    flag = True

                    for k in range(len(lb)):
                        if lb[k] != data[i + k]:
                            flag = False
                            break
                    
                    if flag:
                        low_count += 1

                hb = high_bit[j]
                if len(hb) <= len(data) - i:
                    flag = True

                    for k in range(len(hb)):
                        if hb[k] != data[i + k]:
                            flag = False
                            break
                    
                    if flag:
                        high_count += 1

        if low_count == high_count:
            print("GOOD")
        elif low_count > high_count:
            print(f"HIGH {low_count - high_count}")
        else:
            print(f"LOW {high_count - low_count}")


if __name__ == "__main__":
    solve()