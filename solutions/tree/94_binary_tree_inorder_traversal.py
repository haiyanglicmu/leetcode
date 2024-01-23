from typing import Optional, List
from .utils import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        # traverse(root, result)
        result = traverseWithStack(root)
        return result


def traverse(root: Optional[TreeNode], result: List[int]):
    if root is None:
        return
    traverse(root.left, result)
    result.append(root.val)
    traverse(root.right, result)


def traverseWithStack(root):
    result, stack = [], []
    curr = root

    while curr is not None or len(stack) != 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        # when we pop, we know all the nodes in the left tree has already been traversed
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


def main():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    result = Solution().inorderTraversal(root)
    print(result)


main()
