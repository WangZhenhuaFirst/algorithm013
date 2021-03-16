'''
https://leetcode-cn.com/problems/triangle/description/

120. 三角形最小路径和（亚马逊、苹果、字节跳动在半年内面试考过）

思路：
相邻节点：与(i,j)相邻的节点为(i+1,j)和(i+1,j+1)


1.暴力递归：n层， O(2^N)
f(i,j) = min(f(i+1,j), f(i+1,j+1)) + triangle[i][j]
2.递归+记忆：
3.动态规划：O(N^2), N为三角形的行数
将 自顶向下的递归 改为 自底向上的递推
悟：递归是一种自顶向下的思考方式，我先不管子问题具体如何才能解决，先假设子问题可以解决。
然后把整个问题分解成子问题，子问题再分解成更小的子问题。
动态规划是自底向上的思考方式，我是从第一步 一步步 从前往后跑，每走一步，都去掉重复的。其实这种走路的问题，
从前往后和从后往前是一样的。动态规划和递归的关键区别是，动态规划是自底向上的。
重复性（分治) problem(i,j) = sub(i+1,j)
状态转移方程：dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]



https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)
'''


def minimumTotal(triangle: List[List[int]]) -> int:
    '''空间复杂度O(N^2)'''
    if not triangle:
        return
    # triangle 是个不规则的形状，或者说每一行的元素个数不同
    # 如果定义 dp = [[0] * n for _ in range(m)] 之类的，则 for i for j 的范围不好表达
    # 这里直接定义 dp = triangle,看似精妙，其实只是回归 本来就应该的样子
    dp = triangle
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]


def minimumTotal(triangle: List[List[int]]) -> int:
    '''空间复杂度O(N)'''
    if not triangle:
        return
    mini = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            mini[j] = triangle[i][j] + min(mini[j], mini[j+1])
    return mini[0]
