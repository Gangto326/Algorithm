import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    # 2x2 는 1x1 4장으로 변환 가능. 이외는 불가능
    """
    pages = [[{1: 36}],
            [{2: 9}],
            [{3: 4}, {3: 3, 2: 1, 1: 5}, {3: 2, 2: 3, 1: 6}, {3: 1, 2: 5, 1: 7}], 
            [{4: 1, 2: 5}], 
            [{5: 1, 1: 11}]]
    """
    num_list = [0] + [int(next(iterator)) for _ in range(6)]

    answer = num_list[6]
    for i in range(5, 0, -1):
        while i == 5 and num_list[i]:
            num_list[i] -= 1

            if num_list[1]:
                num_list[1] = max(0, num_list[1]-11)
            answer += 1
        
        while i == 4 and num_list[i]:
            num_list[i] -= 1

            two_count = min(5, num_list[2])
            if num_list[2]:
                num_list[2] = max(0, num_list[2] - 5)

            num_list[1] = max(0, num_list[1]-(4*(5-two_count)))
            answer += 1
        
        while i == 3 and num_list[i]:
            if num_list[i] >= 4:
                num_list[i] -= 4
            
            elif num_list[i] == 3:
                num_list[i] -= 3

                if num_list[2]:
                    num_list[2] -= 1
                    num_list[1] = max(0, num_list[1]-5)
                
                else:
                    num_list[1] = max(0, num_list[1]-9)
            
            elif num_list[i] == 2:
                num_list[i] -= 2

                two_count = min(3, num_list[2])
                if num_list[2]:
                    num_list[2] = max(0, num_list[2] - 3)
                
                num_list[1] = max(0, num_list[1]-(4*(3-two_count) + 6))

            elif num_list[i] == 1:
                num_list[i] -= 1

                two_count = min(5, num_list[2])
                if num_list[2]:
                    num_list[2] = max(0, num_list[2] - 5)
                
                num_list[1] = max(0, num_list[1]-(4*(5-two_count) + 7))

            answer += 1

        while i == 2 and num_list[i]:
            two_count = min(9, num_list[2])
            num_list[i] -= two_count
            num_list[1] = max(0, num_list[1]-(4*(9-two_count)))

            answer += 1
        
        while i == 1 and num_list[i]:
            num_list[i] = max(0, num_list[i] - 36)

            answer += 1
                
    print(answer)


if __name__ == "__main__":
    solve()