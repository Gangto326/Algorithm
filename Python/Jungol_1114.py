import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    color_list = list(read().strip()) * 2
    answer = 0

    for i in range(N):
        total = 0
        start_color = color_list[i]
        flag = True

        for j in range(i, N + i):
            if color_list[j] == "w":
                total += 1
            
            else:
                if start_color == "w":
                    start_color = color_list[j]
                    total += 1
                
                else:
                    if start_color == color_list[j]:
                        total += 1
                    
                    else:
                        if flag:
                            start_color = color_list[j]
                            total += 1
                            flag = False

                        else:
                            break
        
        answer = max(answer, total)
                
    print(answer)


if __name__ == "__main__":
    solve()