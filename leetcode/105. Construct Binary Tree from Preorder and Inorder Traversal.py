'''

[1,2,3,4,5,6] - preorder
[3,2,4,1,5,6] - inorder


    1
   / \
  2   5
 / \   \
3   4   6



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inOrder, preOrder, inStrt, inEnd): 
	
	if (inStrt > inEnd): 
		return None

	tNode = Node(preOrder[buildTree.preIndex]) 
	buildTree.preIndex += 1

	if inStrt == inEnd : 
		return tNode 

	inIndex = search(inOrder, inStrt, inEnd, tNode.val) 
	
	tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex- 1) 
	tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd) 

	return tNode 


def search(arr, start, end, value): 
	for i in range(start, end + 1): 
		if arr[i] == value: 
			return i 


def printInorder(node): 
	if node is None: 
		return
	
	printInorder(node.left) 
	
	print(node.val) 

	printInorder(node.right) 

inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1) 

print ("Inorder traversal of the constructed tree is")
printInorder(root) 
