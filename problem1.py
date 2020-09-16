class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root,0)]
        
        while queue:
            dec = 0
            temp = []
            for root, level in queue:
                if root.left and root.left.val in [x,y]:
                    if root.right and root.right.val in [x,y]:
                        return False
                    dec += 1
                if root.left:
                    temp.append((root.left, level+1))
                    
                if root.right and root.right.val in [x,y]:
                    dec += 1
                if root.right:
                    temp.append((root.right, level+1))
                    
            # print(dec, temp)
            if dec == 2:
                return True
            queue = temp
            # print(queue)
        return False