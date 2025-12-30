import sys

read = sys.stdin.readline

cost_list = [2, 3, 5, 7]
cost_total = [100, 9900, 1000000-10000, float('inf')]


def caculator(target):
    global cost_list, cost_total

    w = 0
    for i in range(4):
        if target <= cost_total[i]:
            w += target * cost_list[i]
            break
        else:
            w += cost_total[i] * cost_list[i]
            target -= cost_total[i]
    
    return w



while True:
    A, B = map(int, read().split())

    if A == 0 and B == 0:
        break

    W = 0
    for i in range(4):
        if A <= cost_total[i] * cost_list[i]:
            W += A // cost_list[i]
            break
        else:
            W += cost_total[i]
            A -= cost_total[i] * cost_list[i]



    left = 0
    right = W

    while left < right:
        mid = (left + right) // 2
        my_w = caculator(mid)
        other_w = caculator(W-mid)

        if other_w - my_w > B:
            left = mid + 1
        else:
            right = mid

    print(caculator(left))