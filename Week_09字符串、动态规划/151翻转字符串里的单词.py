'''
https://leetcode-cn.com/problems/reverse-words-in-a-string/

151. 翻转字符串里的单词（微软、字节跳动、苹果在半年内面试中考过）

思路：
2. reverse整个string，再单独reverse每个单词












'''


def reverseWords(self, s: str) -> str:
    '''
    split，reverse，join
    O(N)
    O(N)
    '''
    # reversed 函数返回一个反转的迭代器
    return ' '.join(reversed(s.split()))


def reverseWords(self, s: str) -> str:
    '''split，reverse，join'''
    return ' '.join(s.split()[::-1])


def reverseWords(self, s: str) -> str:
    '''双指针， 空间O(N)'''
    s = s.strip()  # 删除首尾空格
    i = j = len(s) - 1
    res = []
    while i >= 0:
        while i >= 0 and s[i] != ' ':
            i -= 1
        res.append(s[i+1:j+1])
        # 如果第一个单词后 就没空格了，i 就直接 == 0 了，后面也就不会执行了
        while s[i] == ' ':  # 跳过单词间空格
            i -= 1
        j = i
    return ' '.join(res)


def reverseWords(self, s: str) -> str:
    ls = self.trim_spaces(s)

    # 翻转字符串
    self.reverse(ls, 0, len(ls) - 1)

    # 翻转每个单词
    self.reverse_each_word(ls)

    return ''.join(ls)


def trim_spaces(self, s: str) -> list:
    left, right = 0, len(s) - 1
    # 去掉字符串开头的空白字符
    while left <= right and s[left] == ' ':
        left += 1

    # 去掉字符串末尾的空白字符
    while left <= right and s[right] == ' ':
        right -= 1

    # 将字符串间多余的空白字符去除
    output = []
    while left <= right:
        if s[left] != ' ':
            output.append(s[left])
        elif output[-1] != ' ':
            output.append(s[left])
        left += 1

    return output


def reverse(self, l: list, left: int, right: int) -> None:
    while left < right:
        l[left], l[right] = l[right], l[left]
        left, right = left + 1, right - 1


def reverse_each_word(self, l: list) -> None:
    n = len(l)
    start = end = 0

    while start < n:
        # 循环至单词的末尾
        while end < n and l[end] != ' ':
            end += 1
        # 翻转单词
        self.reverse(l, start, end - 1)  # 这个过程中，单词之间的空格并没用动，还存在呢
        # 更新start，去找下一个单词
        start = end + 1
        end += 1
