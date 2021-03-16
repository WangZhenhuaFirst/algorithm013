'''
https://leetcode-cn.com/problems/valid-parentheses/

20. 有效的括号（亚马逊、JPMorgan 在半年内面试常考）

思路：
洋葱，最近相关性，stack
先来后到，公平性，queue


1.暴力：不断用空串replace匹配的括号，O(N^2)

2.stack：所有括号问题 都是洋葱问题，用栈即可
栈先入后出的特点 正好与本题括号排序特点一致，
即遇到左括号入栈，遇到右括号时 将对应栈顶左括号出栈，
则遍历完所有括号后 stack 仍为空

只需要遍历一遍，时间复杂度为O(N)

'''


class Solution:
    def is_valid(self, s):
        # 哈希表构建左右括号的对应关系，这样查询两个括号是否对应 只需  O(1)
        dic = {'{': '}', '(': ')', '[': ']', '?': '?'}
        # 栈为空时，stack.pop()会报错，所以给stack加一个元素
        # 防止输入为 ']'这种情况
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            # 如果满足这个if，说明这个右括号，在栈中/或者说在前面的字符串中 没有对应的左括号
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1  # 是为了防止字符中 111左括号比右括号多的情况，如 '['
