'''
Height of binary tree : total number of edges along the longest path from root to the leaf node

Hypothesis : if previous node(left or right) calculate the height, then adding 1 (which is for root node)
then we have total height of binary tree.

Base case : if after recursion we reach the leaf node, return 0
'''


class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 



def get_hbt(root:TreeNode):
    if root == None:
        return -1 

    left = get_hbt(root.left)
    right = get_hbt(root.right) 

    return max(left, right) + 1 # 1 for root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5) 

print("Height of the tree:", get_hbt(root))

