'''
https://leetcode-cn.com/problems/to-lower-case/

709. 转换成小写字母 （谷歌在半年内面试中考过）

思路：













'''


def toLowerCase(self, str: str) -> str:
    '''
    'A' - 'Z' 对应的 ascii 是 65 - 90；
    'a' - 'z' 对应的 ascii 是 97 - 122；
    大小写字母转换相差32，解题只要记住ord(),chr()函数即可
    '''
    s = []
    for c in str:
        if 'A' <= c <= 'Z':
            s.append(chr(ord(c) + 32))
        else:
            s.append(c)
    return ''.join(s)


def toLowerCase(self, str: str) -> str:
    '''PythonIC写法'''
    return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in str])


def toLowerCase(self, str: str) -> str:
    dic = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
           'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
           'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
           'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
           'Y': 'y', 'Z': 'z'}
    s = []
    for c in str:
        if c in dic:
            s.append(dic[c])
        else:
            s.append(c)
    return ''.join(s)


def toLowerCase(self, str: str) -> str:
    '''PythonIC写法'''
    dic = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
           'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
           'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
           'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
           'Y': 'y', 'Z': 'z'}
    return ''.join([dic.get(c, c) for c in str])
