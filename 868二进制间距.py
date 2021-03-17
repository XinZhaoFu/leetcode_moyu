"""
给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。

如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。

输入：n = 22
输出：2
解释：
22 的二进制是 "10110" 。
在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
第一对相邻的 1 中，两个 1 之间的距离为 2 。
第二对相邻的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
"""


class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_length = 0
        temp_length = float('-inf')

        while n:
            if n % 2 == 0:
                temp_length += 1

            else:
                max_length = max(temp_length, max_length)
                temp_length = 1

            n = n // 2

        return max_length
