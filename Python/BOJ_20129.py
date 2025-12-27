import sys

read = sys.stdin.readline
plus, minus, power, division = map(int, read().split())
operator_list = [0] * 4
operator_list[4-plus] = '+'
operator_list[4-minus] = '-'
operator_list[4-power] = '*'
operator_list[4-division] = '/'

expression = read().rstrip()
expression_list = []
num = ''
for i in expression:
    if i == '+'  or i == '-' or i == '*' or i == '/':
        expression_list.append(int(num))
        expression_list.append(i)
        num = ''
    else:
        num += i
expression_list.append(int(num))

for operator in operator_list:
    next_list = []

    while expression_list:
        expression = expression_list.pop()
        
        if expression == operator:
            before_num = next_list.pop()
            next_num = expression_list.pop()

            if operator == '+':
                next_list.append(before_num+next_num)
            elif operator == '-':
                next_list.append(before_num-next_num)
            elif operator == '*':
                next_list.append(before_num*next_num)
            else:
                num = abs(before_num) // abs(next_num)
                if (before_num < 0) ^ (next_num < 0):
                    num = -num
                next_list.append(num)
        else:
            next_list.append(expression)
    
    expression_list = list(reversed(next_list))

print(expression_list[0])