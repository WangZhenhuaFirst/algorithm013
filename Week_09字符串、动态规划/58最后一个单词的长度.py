'''
https://leetcode-cn.com/problems/length-of-last-word/

58. 最后一个单词的长度 （苹果、谷歌、字节跳动在半年内面试中考过）

思路：从字符串末尾开始向前遍历，有两种情况
第一，"Hello World"，从后向前遍历直到遍历到头或遇到空格为止，即为最后一个单词"World"的长度5
第二，"Hello World "，需要先将末尾的空格过滤掉，再进行第一种情况的操作
综合两种情况，先从后过滤掉空格找到单词尾部，再从单词尾部向前遍历，找到单词头部










'''


def lengthOfLastWord(self, s: str) -> int:
    '''
    no splits, no len() calls, 
    just a simple loop and two variables

    scan from the end, increment the length counter if non-space found,
    otherwise keep skipping spaces break and return the counter if space
    encountered AFTER we found any non-sapce
    '''
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            count += 1
        # elif中暗含着s[i] == ' ',所以其实是 elif s[i] == ' ' and count > 0
        # 已经count了若干个字母之后，再遇到空格，直接 break
        elif count > 0:
            break
        # 另一种情况是 s[i] == ' ' ，并且 count = 0,啥也不做，继续遍历下一个位置
    return count


def lengthOfLastWord(self, s: str) -> int:
    '''split库函数'''
    # 如果s = ' '，只有一个空格，则 if s 为TRUE
    # 而此时 s.split()得到的是个空数组[]
    # 所以要在split()之后再判断是否为空
    s = s.split()
    return len(s[-1]) if s else 0
