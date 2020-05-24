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
