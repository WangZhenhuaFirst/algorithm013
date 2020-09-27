'''
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

557. 反转字符串中的单词III （微软、字节跳动、华为在半年内面试中考过）

思路：



'''


def reverseWords(self, s: str) -> str:
    '''将字符串分割成单词列表 然后把每个单词反转切片'''
    return ' '.join(word[::-1] for word in s.split(' '))


def reverseWords(self, s: str) -> str:
    '''利用两次切片，不需遍历'''
    return ' '.join(s.split(' ')[::-1])[::-1]


def reverseWords(self, s: str) -> str:
    '''先反转字符串，再反转单词列表'''
    return ' '.join(s[::-1].split(' ')[::-1])
