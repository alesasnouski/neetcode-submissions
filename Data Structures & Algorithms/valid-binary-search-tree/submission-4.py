class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(rt, minVal, maxVal):
            if rt:
                return rt.val > minVal and rt.val < maxVal and isValid(rt.left, minVal, rt.val) and isValid(rt.right, rt.val, maxVal)
            else:
                return True
        
        return isValid(root, float("-inf"), float("inf"))