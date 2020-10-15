'''
https://leetcode-cn.com/problems/walking-robot-simulation/description/

874. 模拟行走机器人

思路：模拟机器人行走过程，计算每一步坐标点到原点的欧式距离的平方，与保存的最大值比较，实时更新最大值。














'''


def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    # 怎么朝着某个方向走出一步？竖着看dx和dy，
    # 向北，x不动，y+1,即（0，1）
    # 向东,x+1,y不动，即（1，0）
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # x, y 表示出发的左边为(0,0)
    # di表示当前方向,题目中说了，一开始面向北方，所以di=0表示北方
    # 同时，dx、dy的下标 代表当前方向
    x = y = di = 0
    obstacleSet = set(map(tuple, obstacles))
    ans = 0
    for cmd in commands:
        if cmd == -2:  # left
            di = (di - 1) % 4
        elif cmd == -1:  # 右转90度，只要当前方向+1即可得到右转方向
            di = (di + 1) % 4
        else:
            for k in range(cmd):
                if (x+dx[di], y+dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    ans = max(ans, x*x + y*y)
    return ans
