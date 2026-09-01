import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    point_list = [tuple(map(int, read().split())) for _ in range(N)]
    answer_list = []


    def orientation(a, b, c):
        cross = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return cross


    def combination(index, li, count):
        nonlocal N

        if count == 3:
            if not orientation(point_list[li[0] - 1], point_list[li[1] - 1], point_list[li[2] - 1]):
                answer_list.append(" ".join(map(str, li)))
            return
        
        if index >= N:
            return
        
        for i in range(index, N):
            li.append(i + 1)
            combination(i + 1, li, count + 1)
            li.pop()
    

    combination(0, [], 0)

    print(len(answer_list))
    print("\n".join(answer_list))


if __name__ == "__main__":
    solve()