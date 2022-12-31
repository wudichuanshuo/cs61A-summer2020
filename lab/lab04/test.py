def tree(label, branches=[]):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def count(n, m):
    if n == 0:
        return 1
    elif n <= 0 or m == 0:
        return 0
    else:
        return count(n - m, m) + count(n, m - 1)


def right_binarize(tree):
    """Construct a right-branching binary tree."""
    assert is_tree(tree), 'must be tree'
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]
    