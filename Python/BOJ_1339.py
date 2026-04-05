import sys

def solve():
    read = sys.stdin.readline
    N = int(read())

    alpha_dict = {}
    for _ in range(N):
        word = read().strip()

        disit = 1
        for i in range(1, len(word) + 1):
            if word[-i] in alpha_dict:
                alpha_dict[word[-i]] += disit
            
            else:
                alpha_dict[word[-i]] = disit

            disit *= 10

    num = 9
    answer = 0
    for i in sorted(alpha_dict.values(), reverse = True):
        answer += i * num
        num -= 1

    print(answer)


if __name__ == "__main__":
    solve()