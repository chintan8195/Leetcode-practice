# Asked in bloomberg | Phone interview

# https://leetcode.com/discuss/interview-question/625192/Bloomberg-or-Phone-or-Entity-Ownership

'''
https://assets.leetcode.com/users/kmsharmausa14/image_1589135817.png

If the graph is given as illustrated in the highlighted section, how will you use it to draw the table below it which displays Parent, Child and their ownerships % mapped (Parent to Child).

Example :

Suppose initially A has 100
According to the figure A--B = 50 %, table shows A - B = 50 % (which is 50 % of A's 100)
then According to the figure B--D = 50 %, table shows A - D = 25 % (which is 50 % of B's 50)
then According to the figure D--G = 10 %, table shows A - G = 2.5 % (which is 10 % of D's 25)

that's what is shown in the table.
I started creating a TreeNode with the node name 'A' etc. and its percentage and left and right child. Interviewer was ok with that. You need to print the same table. Hope that help !

'''
class Node:
    def __init__(self, letter, p):
        self.letter = letter
        self.left = None
        self.right = None
        self.percentage = p

class Solution:
    def __init__(self):
        self.entity_table = {}


    def recurse(self, parent_letter, root, entity_val):
        if not root:
            return

        new_entity_val = root.percentage*entity_val*0.01

        try:
            self.entity_table[parent_letter].append((root.letter, new_entity_val))
        except KeyError:
            self.entity_table[parent_letter] = [(root.letter, new_entity_val)]


        if root.left:
            self.recurse(parent_letter, root.left, new_entity_val)

        if root.right:
            self.recurse(parent_letter, root.right, new_entity_val)




    def find_entity_ownership(self, root):
        nodes = [root]
        que = [root]

        while que:

            que_len = len(que)

            for i in range(0, que_len):
                parent = que[i]

                if parent.left:
                    que.append(parent.left)
                    nodes.append(parent.left)

                if parent.right:
                    que.append(parent.right)
                    nodes.append(parent.right)

            que = que[que_len:]

        for node in nodes:
            root_node = node
            root_letter = root_node.letter

            self.recurse(root_letter, root_node.left, 100)
            self.recurse(root_letter, root_node.right, 100)

        return self.entity_table



if __name__ == "__main__":
    root = Node("A", 100)
    root.left = Node("B", 50)
    root.right =Node("C", 33)
    root.left.left = Node("D", 50)
    root.left.right = Node("F", 30)
    root.left.left.left = Node("G", 10)
    root.right.right = Node("E", 10)
    x = Solution().find_entity_ownership(root)
    print(x)