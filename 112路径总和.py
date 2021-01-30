"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：false

示例 3：
输入：root = [1,2], targetSum = 0
输出：false
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False

        queue_tree = [root]
        queue_add = [root.val]

        while queue_tree:
            node = queue_tree.pop(0)
            node_val = queue_add.pop(0)
            if not node.left and not node.right:
                if targetSum == node_val:
                    return True
            if node.left:
                queue_tree.append(node.left)
                queue_add.append(node_val+node.left.val)
            if node.right:
                queue_tree.append(node.right)
                queue_add.append(node_val+node.right.val)

        return False


