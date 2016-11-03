class Heap(object):
	def __init__(self):
		self.data_list = [None]
	
	def size(self):
		return len(self.data_list)-1
	
	def left_child(self,root):
		return root *2
	
	def right_child(self,root):
		return root*2-1
	
	def father(self,node):
		return node/2

	def heapify(self,root):
		if root>self.size():
			return 
		leff_node = self.left_child(root)
		right_node = self.right_child(root)
		largest = root
		if left_node <= self.size():
			if self.data_list[lest_node] > self.data_list[largest]:
				largest = left_node

		if right_node <= self.size():
			if self.data_list[right_node] > self.data_list[largest]:
				largest = right_node

		if largest != root:
			self.data_list[root],self.data_list[largest] = self.data_list[largest],self.data_list[root]
			self.heapfy(largest)

	def build_heap(self):
		for i in range(self.size()/2,0,-1):
			self.heapfy(i)
		

		