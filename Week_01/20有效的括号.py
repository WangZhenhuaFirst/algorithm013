'''
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true


解题思路：
洋葱，最近相关性，stack
先来后到，公平性，queue


1.暴力：不断用空串replace匹配的括号，O(N^2)

2.stack：所有括号问题都是洋葱问题，用栈即可
栈先入后出的特点正好与本题括号排序特点一致，
即遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，
则遍历完所有括号后 stack 仍为空

只需要遍历一遍，时间复杂度为O(N)
'''


class Solution:
    def is_valid(self, s):
        # 哈希表构建左右括号的对应关系，这样查询两个括号是否对应只需  O(1)
        dic = {'{': '}', '(': ')', '[': ']'}
        # 栈为空时，stack.pop()会报错，所以给stack加一个元素
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == "__main__":
    so = Solution()
    s = "()[]{}"
    print(so.is_valid(s))
