# Walk down the tree from the top.
# Draw a few perfect binary trees.
# By height = 5, notice the pattern that for any node with the following properties:
#   1. having children, 
#   2. having value n, 
#   3. having height H, 
# that node's right child is valued n-1 and its left child is valued n - 2^(H-1).
# Also notice that with this post ordering notation, all nodes marked greater than the left node are contained under the right node.
# Use these two facts in order to walk down the tree while keeping only the value of the current node and its height in memory.
# Additionally we have the property that "runs" of consecutive values move down the right children under a node.
# Use this fact to quickly get the parent of any node of value n at height H having value from n to n - H - 1.

def find_parent_in_bounds(height, target, parent):
    # Take advantage of runner property if target is in runner range
    if target in range(parent-height+1, parent):
        return(target+1)
    else:
        left_val = parent - 2**(height-1)
        # Return parent if target = left node
        if target == left_val: 
            return(parent)
        else:
            # Go right if target > left node
            if target > left_val:
                return(find_parent_in_bounds(height-1, target, parent-1))
            # Go left if target < left node
            else:
                return(find_parent_in_bounds(height-1, target, left_val)) 

def find_parent(height, target):
    if ((height == 1) or not (target in range(1, -1+2**height))):
        return(-1)
    else: 
        return(find_parent_in_bounds(height, target, -1+2**height))

def answer(h, q):
    return [find_parent(h, x) for x in q]

