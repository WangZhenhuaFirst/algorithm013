'''
https://leetcode-cn.com/problems/jewels-and-stones/

771. 宝石与石头 （亚马逊在半年内面试中考过）

思路：













'''


def numJewelsInStones(self, J: str, S: str) -> int:
    '''朴实无华'''
    count = 0
    for c in S:
        if c in J:
            count += 1
    return count


def numJewelsInStones(self, J: str, S: str) -> int:
    return len([x for x in S if x in J])


def numJewelsInStones(self, J: str, S: str) -> int:
    '''O(len(J) * len(S))'''
    return sum(x in J for x in S)
