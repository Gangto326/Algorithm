import sys

def solve():
    read = sys.stdin.readline
    T = int(read().rstrip())

    for tc in range(T):
        N = int(read().rstrip())
        check = set()
        answer = "YES"

        for _ in range(N):
            phone_number = read().rstrip()
            check.add(phone_number)

        for phone_number in check:
            for i in range(len(phone_number)):
                if phone_number[:i] in check:
                    answer = "NO"
                    break
            
            if answer == "NO":
                break
        
        print(answer)


if __name__ == "__main__":
    solve()