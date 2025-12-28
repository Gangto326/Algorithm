import sys

read = sys.stdin.read().split()
iterator = iter(read)

left_set = set()
right_set = set()
read_set = set()

def wait():
    global left_set, right_set, read_set

    print('WAIT')
    left_set = set()
    right_set = set()
    read_set = set()


while True:
    query = next(iterator)

    if query == 'EXIT':
        print('EXIT')
        break
    elif query == 'WRITE':
        left, to, right = next(iterator), next(iterator), next(iterator)

        if left in right_set:
            wait()
        elif right in right_set:
            wait()
        elif (right in read_set) or (right in left_set):
            wait()
        
        left_set.add(left)
        right_set.add(right)
        print(query + " " + left + " " + to + " " + right)
    else:
        node = next(iterator)
        
        if node in right_set:
            wait()
        
        read_set.add(node)
        print(query + " " + node)