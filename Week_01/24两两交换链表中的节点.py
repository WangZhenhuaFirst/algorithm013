'''
https://leetcode-cn.com/problems/swap-nodes-in-pairs/

24. 两两交换链表中的节点

思路：
1.递归：O(N)
递归本质就是不断重复相同的事情。不要去思考完整的调用栈，你想不明白。
我们应该关心的有三点：
返回值：交换完成的子链表
调用单元：
终止条件：head为空指针(无节点)或next为空指针(只有一个节点了，无法交换了)

2.迭代








'''


class Solution:
    def swapPairs(self, head: ListNode):
        '''递归'''
        # 每一层递归，如果没有需要交换的节点了，就return head
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        # 每一层递归，如果有需要交换的节点，就交换完，然后return second_node 给上一层递归用
        # 或者可以这样说：交换了两个节点以后，返回 secondNode，因为它是交换后的新头
        return second_node

    def swapPairs(self, head: ListNode):
        '''迭代，前面加一个辅助节点'''
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            # 交换
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # 交换过后，指向节点3 的是 节点1
            prev_node = first_node
            head = first_node.next
        # 因为一开始把dummy赋值给了prev_node，所以操作的是prev_node,
        # dummy的指向一直没变
        return dummy.next
