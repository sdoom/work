class Node(object):
	def __init__(self,index):
		self.index = index
		self.leftchild = None
		self.rightchild = None
class BinaryTree(object):
	def __init__(self,root):
		self.root = root
	def pre_travel(self,node):
		if not node:
			return 
		print (node.index)
		self.pre_travel(node.leftchild)
		self.pre_travel(node.rightchild)
	def medium_travel(self,node):
		if not node:
			return
		print(node.index)
		self.medium_travel(node.leftchild)
		self.medium_travel(node.rightchild)

node_dict = {}
for i in range(1,10):
	node_dict[i] = Node(i)
node_dict[1].leftchild = node_dict[2]
node_dict[1].rightchild = node_dict[3]
node_dict[2].leftchild = node_dict[5]
node_dict[2].rightchild = node_dict[6]
node_dict[3].leftchild = node_dict[7]
node_dict[7].leftchild = node_dict[8]
node_dict[7].rightchild = node_dict[9]

tree =  BinaryTree(node_dict[1])
#tree.pre_travel(tree.root)
tree.medium_travel(tree.root)

	



