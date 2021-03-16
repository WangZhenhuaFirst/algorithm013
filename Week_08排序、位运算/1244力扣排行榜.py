'''
https://leetcode-cn.com/problems/design-a-leaderboard/

1244.力扣排行榜 （Bloomberg 在半年内面试中考过）

思路：













'''


class leaderboard:
    def __init__(self):
        self.dic = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] = self.dic.get(playerId, 0) + score

    def top(self, K: int) -> int:
        s = sorted([v for v in self.dic.values()], reverse=True)
        return sum(s[:K])

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0
