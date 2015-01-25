from node import node
'''tree = node("grandmother", [
		node("daughter", [
			node("granddaughter"),
			node("grandson")]),
		node("son", [
			node("granddaughter"),
			node("grandson")]),
		node("abc")
		])'''
tree = node('abc')
#tree.addlist(['xyz','abc'])
#temp_node = tree.search('abc')
#temp_node.addnode('xyz')
tree.addnode('xyz')
print tree
