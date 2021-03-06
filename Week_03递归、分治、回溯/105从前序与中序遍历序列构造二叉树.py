'''
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

105. 从前序与中序遍历序列构造二叉树 （字节跳动、亚马逊、微软在半年内面试中考过）


思路：可以用递归完成












'''


class Solution:
    def buildTree(self, preorder, inorder):
        # 递归的终止条件
        if not inorder:
            return None

        # 递归对本层的处理
        root = TreeNode(preorder.pop(0))  # 前序遍历的第一个元素为根节点
        mid = inorder.index(root.val)  # 中序遍历中，根节点左侧为左子树，右侧为右子树

        # 构建二叉树本质上是：找到各子树的根节点，构建该根节点的左子树，构建该根节点的右子树
        # 不要去想每一层的递归是如何执行的，那很难想明白。
        # 这样去想：把相应的preorder、inorder参数传给下一层
        root.left = self.buildTree(preorder, inorder[:mid])
        # 虽然每一层的递归都不会立即执行完return root，还都压在栈中呢
        # 但每一层的root = TreeNode(preorder.pop(0))都是立即执行了的，所以preorder一直在改变
        root.right = self.buildTree(preorder, inorder[mid+1:])

        # 除了最后一层递归return None之外，其它的都return root给上一层，作为上一层root的left或right
        return root
