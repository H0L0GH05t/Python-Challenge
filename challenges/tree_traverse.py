"""
Given a deeply nested dict, create a function that returns a
value within a tree when given the tree and a key. If there are
duplicates, the first result found should be returned.

    {
        'a': {
            'b': 123,
            'c': 456,
            'd': {
                'z': 789,
            },
        },
        'x': {
            'y': 111,
        },
    }  # input of 'z' should return '789'

"""


def tree_traverse(tree, key):
    for node in tree:
        if node == key:
            # found the key, so return the value
            return tree[node]
        elif isinstance(tree[node], dict):
            # didn't find the key, so continue deeper if possible
            result = tree_traverse(tree[node], key)
            
            # if the result is found nested, return the value found here
            if result:
                return result
