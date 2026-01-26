import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve():
    num_list = list(map(int, sys.stdin.read().split()))

    def DFS(num_list):
        if not num_list:
            return None
        
        root_val = num_list[0]
        root = Node(root_val)
        
        index = len(num_list)
        for i in range(index):
            if num_list[i] > root_val:
                index = i
                break

        root.left = DFS(num_list[1:index])
        root.right = DFS(num_list[index:])

        return root
    

    root_node = DFS(num_list)


    def post_order(node):
        
        if node.left == None and node.right == None:
            print(node.val)
            return
        
        if node.left != None:
            post_order(node.left)
        
        if node.right != None:
            post_order(node.right)
        
        print(node.val)


    post_order(root_node)


if __name__ == "__main__":
    solve()