'''
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

236. 二叉树的最近公共祖先 （Facebook在半年内面试常考）   ？？？

思路：O(N)
祖先：若节点p在节点root的左/右子树中，或p = root，则称root 是 p 的祖先
最近公共祖先：设节点root为节点p、q的某公共祖先，若其左子节点 root.left 和右子节点 root.right 
都不是p、q的公共祖先，则称root是 p、q的最近公共祖先

若root 是 p、q的 最近公共祖先，又因为题目中规定p != q, 则只可能为以下情况之一：
p和q在root的子树中，且分列在root的异侧
p = root，且q在root的左或右子树中
q = root,且p在root的左或右子树中

由于需要先知道左右子树的情况，然后决定向上返回什么。因此使用后序遍历，遇到p或q时返回。
从底至顶回溯，当p、q在节点root的异侧时，节点root即为最近公共祖先，则向上返回root。



'''


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # 这里的root不一定指最初的root，而只是指node

    # 递归终止条件:如果当前节点为空或等于p/q，则返回当前节点
    if not root or root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    # 以下这几种情况，每一层都会执行，层层向上返回

    # 如果左右子树 其中一个不为空，则返回非空节点
    if not left:
        return right
    if not right:
        return left
    # 递归遍历左右子树，如果左右子树查到的节点 都不为空，表明p 和 q 分别在左右子树中
    # 因为递归的终止条件是 节点为空或等于p/q时 返回，既然返回的left/right都不为空，说明返回的是p和q
    # 因此当前节点即为最近公共祖先
    return root
