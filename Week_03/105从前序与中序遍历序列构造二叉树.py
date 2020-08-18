'''
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:你可以假设树中没有重复的元素。


思路：
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/python-di-gui-xiang-jie-by-jalan/
前序遍历的第一个元素为根节点
中序遍历中，根节点左侧为左子树，右侧为右子树

构建二叉树本质上是：
找到各子树的根节点
构建该根节点的左子树
构建该根节点的右子树

可以用递归完成
'''


class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])
        return root
