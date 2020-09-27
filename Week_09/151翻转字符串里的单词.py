'''
https://leetcode-cn.com/problems/reverse-words-in-a-string/

151. 翻转字符串里的单词（微软、字节跳动、苹果在半年内面试中考过）

思路：
1. split，reverse，join
2. reverse整个string，再单独reverse每个单词










'''


def reverseWords(self, s: str) -> str:
    '''调用语言的API'''
    return ' '.join(reversed(s.split()))


def reverseWords(self, s: str) -> str:
    '''
    自己实现函数/API
    python 中字符串不可变,首先要把字符串转化为可变的数据结构



    '''
