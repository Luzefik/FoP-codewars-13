"""
# Pre-order traversal
def pre_order(node):
    return [node.data] + pre_order(node.left) + pre_order(node.right) if node else []

# In-order traversal
def in_order(node):
    return in_order(node.left) + [node.data] + in_order(node.right) if node else []

# Post-order traversal
def post_order(node):
    return post_order(node.left) + post_order(node.right) + [node.data] if node else []


Pre-order means that we
1.) Visit the node.
2.) Traverse the left subtree (left node.)
3.) Traverse the right subtree (right node.)

In-order means that we
1.) Traverse the left subtree (left node.)
2.) Visit the node.
3.) Traverse the right subtree (right node.)

Post-order means that we
1.) Traverse the left subtree (left node.)
2.) Traverse the right subtree (right node.)
3.) Visit the node.
"""


# Pre-order traversal
def pre_order(node):
    res = []
    if node is None:
        return res

    stack = [node]

    while stack:
        curr = stack.pop()
        res.append(curr.data)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return res


# In-order traversal
def in_order(node):
    ans = []
    stack = []
    curr = node

    while curr is not None or len(stack) > 0:

        while curr is not None:

            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        ans.append(curr.data)

        curr = curr.right

    return ans


# Post-order traversal
def post_order(node):
    res = []
    st = []
    while True:
        while node:
            st.append(node)
            st.append(node)
            node = node.left
        if not st:
            return res
        node = st.pop()
        if st and st[-1] == node:
            node = node.right
        else:
            res.append(node.data)
            node = None
