import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    bunza_list = list(read().rstrip())

    h_count, o_count = 0, 0
    for i in bunza_list:
        if i == "H":
            h_count += 1
        else:
            o_count += 1

    if h_count != o_count * 2:
        print("mix")
        return

    h_count, o_count = 0, 0
    for i in bunza_list:
        if i == "H":
            h_count += 1
        else:
            o_count += 1

            if o_count > h_count:
                print("mix")
                return
    
    h_count, o_count = 0, 0
    for i in bunza_list[::-1]:
        if i == "H":
            h_count += 1
        else:
            o_count += 1

            if o_count > h_count:
                print("mix")
                return
    
    print("pure")


if __name__ == "__main__":
    solve()