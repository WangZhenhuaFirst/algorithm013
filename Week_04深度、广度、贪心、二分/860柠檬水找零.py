'''
https://leetcode-cn.com/problems/lemonade-change/description/

860. 柠檬水找零（亚马逊在半年内面试中考过）

思路：













'''


def lemonadeChange(self, bills: List[int]) -> bool:
    '''
    记录5和10的个数，如果有一个透支了，就说明不能满足找零
    '''
    count5 = count10 = 0
    for k in bills:
        if k == 5:
            count5 += 1
        elif k == 10:
            if not count5:
                return False
            count10 += 1
            count5 -= 1
        else:
            if count10 and count5:
                count10 -= 1
                count5 -= 1
            elif count5 > 2:
                count5 -= 3
            else:
                return False
    return True
