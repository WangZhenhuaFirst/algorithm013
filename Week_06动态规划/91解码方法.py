'''
https://leetcode-cn.com/problems/decode-ways/

91. 解码方法（Facebook、亚马逊、字节跳动在半年内面试中考过）

思路：
和爬楼梯是同类问题，难点是加了许多限制条件。
去除这些限制条件，就是爬楼梯了，一次可以爬一步，也可以爬两步，问有多少种方式到达终点。

1.递归：把大问题 化作小问题
比如2322，对于第一个字母有两种划分方式： 2|322 和 23|22
假设我们知道了第一种的右半部分的解码方式有 ans1 种，第二种的右半部分的解码方式有 ans2 种，
那么2322 整体的解码方式就是 ans1 + ans2 种。
这个问题类似于：假如从深圳到北京可以经过武汉和上海两条路，而从武汉到北京有8条路，从上海到北京有6条路。
那么从深圳到北京就有 8 + 6 = 14 条路。

2.动态规划：
递归就是自顶向下，压栈、压栈、压栈，出栈、出栈、出栈。
动态规划自底向上，可以省略压栈的过程。
dp[i] 表示以s[i]开头到结尾的 解码方法数
如果s[i] 和s[i+1] 组成的数字<=26，则 dp[i] = dp[i+1] + dp[i+2]
其中,dp[i+1]表示单独解码s[i]; dp[i+2]表示将s[i]和s[i+1]放在一起解码
'''


def numDecodings(s: str) -> int:
    '''递归 + 备忘录'''
    def get_ans(s, start, mem):
        # 划分到最后返回1 ？？？ 为什么是1 而不是0 ？？？
        if start == len(s):
            return 1
        # 开头是 0 ，则不对应任何字母
        if s[start] == '0':
            return 0

        m = mem.get(start, -1)
        if m != -1:
            return m

        # 以任何一个数字作为开头，都可以走一步或两步
        ans1 = get_ans(s, start+1, mem)  # 得到第一种划分的解码方法数
        ans2 = 0

        if start < len(s) - 1:  # 这样才s[start]和s[start+1] 还有元素可取，否则,ans2取默认值0
            if int(s[start:start+2]) <= 26:  # 这时候 start和start+1组合在一起才能解码
                ans2 = get_ans(s, start+2, mem)
        mem[start] = ans1 + ans2
        return ans1 + ans2

    mem = dict()
    return get_ans(s, 0, mem)


def numDecodings(s: str) -> int:
    '''动态规划'''
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1  # 这里的 1，是为了给dp[n-2]用

    # s的最后一个数字如果不是0，那么以它开头的字符串有一种解码方式
    if s[n-1] != '0':
        dp[n-1] = 1
    # 用的反向遍历，如果遇到 0 作为开头，直接continue即可
    # 如果用正向遍历，对于0，需要分成好几种情况
    # 倒序排列还有一个好处，就是和递归的形式几乎一样
    for i in range(n-2, -1, -1):
        # 如果当前数字是0，直接跳过。因为 0 不代表任何字母
        if s[i] == '0':
            continue
        dp[i] = dp[i+1]
        if int(s[i:i+2]) <= 26:
            dp[i] += dp[i+2]
    return dp[0]


def numDecodings(s: str) -> int:
    '''
    空间优化
    求dp[i] 只需要 dp[i+1] 和 dp[i+2]
    '''
    n = len(s)
    end = 1
    cur = 0
    # s的最后一个数字如果不是0，那么以它开头的字符串有一种解码方式
    if s[n-1] != '0':
        cur = 1
    for i in range(n-2, -1, -1):
        # 如果当前数字是0，直接跳过。因为0不代表任何字母
        if s[i] == '0':
            end = cur  # end 前移
            cur = 0
            continue

        ans1 = cur
        ans2 = 0
        if int(s[i:i+2]) <= 26:
            ans2 = end
        end = cur  # end 前移
        cur = ans1 + ans2
    return cur


def numDecodings(self, s: str) -> int:
    '''
    正序遍历
    dp[i] = the number of ways to parse the string s[1:i+1]
    '''
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        if int(s[i-1]) != 0:
            dp[i] = dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[n]
