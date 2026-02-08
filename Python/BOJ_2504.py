import sys

def solve():
    read = sys.stdin.readline().strip()
    stack = []
    multi = 1
    answer = 0

    for i in range(len(read)):
        char = read[i]

        if char == "(":
            stack.append(char)
            multi *= 2
        
        elif char == "[":
            stack.append(char)
            multi *= 3
        
        elif char == ")":
            if not stack or stack[-1] != "(":
                print(0)
                return
            
            if read[i-1] == "(":
                answer += multi

            stack.pop()
            multi //= 2
        
        elif char == "]":
            if not stack or stack[-1] != "[":
                print(0)
                return
            
            if read[i-1] == "[":
                answer += multi
                
            stack.pop()
            multi //= 3

    if stack:
        print(0)
    else:
        print(answer)


if __name__ == "__main__":
    solve()