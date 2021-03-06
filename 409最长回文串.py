"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        dict_s = {}
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        temp = 0
        max_length = 0
        for ch in dict_s.keys():
            length = dict_s[ch]
            if length % 2 == 0:
                max_length += length
            else:
                temp = 1
                max_length += (length - 1)
        max_length += temp

        return max_length

