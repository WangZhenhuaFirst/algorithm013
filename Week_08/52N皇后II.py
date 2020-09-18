'''
https://leetcode-cn.com/problems/n-queens-ii/description/

52. N皇后II （亚马逊在半年内面试中考过）

思路：
参考：https://mp.weixin.qq.com/s/45mfS3ciiVt8nghUSjezFg

column = 10010000
pie    = 00100000
na     = 00101000

'''


def totalNQueens(self, n: int) -> int:
    if n < 1:
        return 0
    self.count = 0
    self.dfs(n, 0, 0, 0, 0)
    return self.count


def dfs(self, n, row, cols, pie, na):
    if row >= n:
        self.count += 1  # 解法加1
        return

    # cols | pie | na，列、撇、捺 方向 所有已经被占的位置 标位1
    # 取反后所有可用的位置标为 1,但cols、pie、na 都是 32位，取反后高位的 0 都变成了 1
    # 而我们只想保留 低8位，想把高位都置为0, ((1<<n) - 1) 表示先把1左移8位——> 100000000
    # 再减1，则变成了 0011111111，再做与运算，即可保留低八位，去除高位
    bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前行 可放置皇后的格子

    while bits:  # bits中还包含1
        p = bits & -bits  # 取到最低位的1，即从当前行可用的格子中取出最右边 为1 的格子
        bits = bits & (bits - 1)  # 将当前行最右边的格子置为0，表示在P位置上放上皇后
        self.dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
