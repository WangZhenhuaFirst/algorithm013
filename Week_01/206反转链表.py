'''
https://leetcode-cn.com/problems/reverse-linked-list/

206. 反转链表


思路：
1.利用外部空间：先申请一个动态扩容的数组或容器，然后遍历链表，将链表中的元素添加到这个容器中。
再利用容器自身的API，反转整个容器。最后同时遍历容器和链表，将链表中的值改为容器中的值。
但空间复杂度不是O(1)

2.双指针迭代：
第一个指针叫pre,最初指向null；
第二个指针叫cur，指向head。然后不断遍历cur,
每次迭代到cur，都将cur的next指向pre，然后pre和cur前进一位。

3.递归：
终止条件是当前节点或下一个节点==null
在函数内部，改变节点的指向，也就是head的下一个节点指向head





'''


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = None
        cur = head
        while cur:
            # 将当前节点指向pre
            # pre 和 cur都前进一个节点
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        # 1->2->3->4->5
        # 如果if 条件不满足，就进入下一层递归
        # 一直递归到链表的最后一个节点，这时候第五层递归满足if条件
        # return head 给第四层递归，第四层递归得到cur = 节点5
        # 在第四层递归中，head.next=节点5，则head为节点4，会继续执行 head.next.next = head
        cur = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        # 而cur不再发生变化，始终是最后一个节点
        return cur
