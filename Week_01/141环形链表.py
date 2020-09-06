'''
https://leetcode-cn.com/problems/linked-list-cycle/

141. 环形链表
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


解题思路：
1.暴力：遍历链表，用set记录下所有节点，看有没有重复的节点出现。
需要用额外的内存，所以空间复杂度不是O(1)

2.快慢指针：如果有环，快指针迟早会追上慢指针。
时间复杂度O(N)，空间复杂度O(1)
'''

from typing import ListNode


class Solution:
    def has_cycle_bad(self, head):
        '''暴力'''
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

    def has_cycle_good(self, head: ListNode):
        i, j = head, head
        # 防止访问 null.next:
        # 如果没环，j指针会先走到头，就不用判断i是否为空；
        # 如果有环，那永远走不到头，也就不必担心为空的问题了
        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    # ？？？Python如何创建链表？？？
    head = [3, 2, 0, -4]
    result = s.has_cycle_good(head)
    print(result)
