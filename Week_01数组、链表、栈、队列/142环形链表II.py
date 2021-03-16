'''
https://leetcode-cn.com/problems/linked-list-cycle-ii/

142. 环形链表II

思路：
1.用set记录下所有节点

2.双指针：这类链表题目一般都是用 双指针 解决的

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
        # 设链表共有 a + b 个节点，其中头部到环入口 a 个， 环 b 个
        # 两指针分别走了f、s步，两指针第一次相遇时，
        # f = 2s
        # f = s + nb fast比slow多走了n个环
        # 以上两式相减得：
        # f = 2nb
        # s = nb
        # 所有走到环入口节点的步数是：k = a + nb
        # 第一次相遇时 slow已经走了nb步，所以让slow再走a步，就会到达 环入口。
        # 也就是说，此时再起一个指针从头开始走，它与slow相遇的地方，就是环入口。
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                start = head
                while start != slow:  # 这里要先判断是否相等，再next
                    start = start.next
                    slow = slow.next
                return slow
        return None
