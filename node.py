class Node:
	def __init__(self, value):
		self.left = []
		self.value = value
		self.right = []
	
	def iterate(self):
    		for node in self.left:
        		yield from node.iterate()
    		yield self.value
    		for node in self.right:
        		yield from node.iterate()

def main():
	root = Node(0)
	root.left = [Node(i) for i in [1,2,3]]
	root.right = [Node(i) for i in [4,5,6]]

	it = root.iterate()
	while True:
    		try:
        		print(it.send(None))
    		except StopIteration:
        		break

if __name__ == "__main__":
	main()
