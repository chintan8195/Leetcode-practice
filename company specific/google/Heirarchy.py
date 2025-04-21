"""
Input:
dog, poodle
mammal, dog
mammal, cat
dog, bulldog
dog, terrier

Output:
mammal
        dog
                poodle
                bulldog
                terrier
        cat
"""

from collections import defaultdict


def print_hierarchy(pairs):
    tree = defaultdict(list)
    children = set()
    nodes = set()

    for parent, child in pairs:
        tree[parent].append(child)
        children.add(child)
        nodes.add(parent)
        nodes.add(child)

    roots = nodes - children

    # Step 3: DFS traversal and print hierarchy
    def dfs(node, depth):
        print("\t" * depth + node)
        for child in sorted(tree[node]):  # sort for consistent output
            dfs(child, depth + 1)

    for root in sorted(roots):  # sort for consistent output
        dfs(root, 0)


pairs = [
    ("dog", "poodle"),
    ("mammal", "dog"),
    ("mammal", "cat"),
    ("dog", "bulldog"),
    ("dog", "terrier"),
    ("cat", "orange tabby"),
    ("avian", "bird"),
    ("bird", "avian")
]

print_hierarchy(pairs)
