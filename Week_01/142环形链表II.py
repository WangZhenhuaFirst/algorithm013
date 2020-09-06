'''
https://leetcode-cn.com/problems/linked-list-cycle-ii/

142. 环形链表 II

1.用set记录下所有节点

2.双指针
# 设链表共有 a + b 个节点，其中头部到环入口 a 个， 环 b 个
# 两指针分别走了f,s步
# f = 2s
# f = s + nb
# f = 2nb
# s = nb

# 所有走到环入口节点的步数是：k = a + nb
# 第一次相遇时slow已经走了nb步

# 只有第二次相遇时，才肯定是相遇在环入口处
'''


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''需要额外空间'''
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        '''双指针'''
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                start = head
                while start != slow:
                    start = start.next
                    slow = slow.next
                return slow
        return None
