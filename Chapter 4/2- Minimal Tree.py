# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBst(self, nums: List[int]) -> Optional[TreeNode]:
        if nums!=[]:
            half = len(nums)//2
            root = TreeNode(nums[half])
            root.left = self.sortedArrayToBst(nums[:half])
            root.right = self.sortedArrayToBst(nums[half+1:])
            return root
        else:
            return None
        
