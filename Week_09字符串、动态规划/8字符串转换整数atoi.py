'''
https://leetcode-cn.com/problems/string-to-integer-atoi/

8. 字符串转换整数 (atoi) （亚马逊、微软、Facebook 在半年内面试中考过）

思路：这个问题 其实没有考察算法的知识，模拟的是日常开发中 对于原始数据的处理（例如「参数校验」等场景），
如果面试中遇到类似的问题，应先仔细阅读题目文字说明和示例，有疑惑的地方和需要和面试官确认，
在编码的时候需要耐心和细心地调试。

其实很多时候，业务需求就是类似这样的问题，工作中如果遇到：
1、有现成的工具和类库需尽量使用，因为它们是性能更优，且经过更严格测试，是相对可靠的；
2、能抽取成工具类、工具方法的尽量抽取，以突出主干逻辑、方便以后代码复用；
3、不得不写得比较繁琐、冗长的时候，需要写清楚注释、体现逻辑层次，以便上线以后排查问题和后续维护。






'''


def myAtoi(self, str: str) -> int:
    '''
    根据示例 1，需要去掉前导空格；
    根据示例 2，需要判断第 1 个字符为 + 和 - 的情况，因此，可以设计一个变量 sign，
    初始化的时候为 1，如果遇到 - ，将 sign 修正为 -1；
    判断是否是数字，可以使用字符的 ASCII 码数值进行比较，即 0 <= c <= '9'；
    根据示例 3 和示例 4 ，在遇到第 1 个不是数字的字符的情况下，转换停止，退出循环；
    根据示例 5，如果转换以后的数字超过了 int 类型的范围，需要截取。这里不能将结果 res变量 设计为 long 类型，
    注意：由于输入的字符串转换以后也有可能超过 long 类型，因此需要在循环内部就判断是否越界，
    只要越界就退出循环，这样也可以减少不必要的计算；
    由于涉及下标访问，因此全程需要考虑数组下标是否越界的情况。
    '''
    # 要先 strip，再判断剩余的 是否为空，防止输入为 空字符串 ' ',导致ls[0]取不到值
    ls = list(str.strip())
    if len(ls) == 0:
        return 0

    if ls[0] == '-':
        sign = -1
    else:
        sign = 1
    if ls[0] in ['-', '+']:
        del(ls[0])
    res, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        res = res * 10 + int(ls[i])
        i += 1
    return max(-2**31, min(sign * res, 2**31 - 1))  # 不要漏掉了sign
