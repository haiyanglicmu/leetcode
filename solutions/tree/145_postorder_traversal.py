from typing import List, Optional
from .utils import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return traverseWithStack(root)[::-1]


def traverseWithStack(root) -> List[int]:
    ans, stack = [], []
    stack.append(root)

    while len(stack) != 0:
        curr = stack.pop()
        # current node -> right node -> left node, so that the reverse order
        # is left -> right -> current
        ans.append(curr.val)
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)
    return ans


def main():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    result = Solution().postorderTraversal(root)
    print(result)


main()
