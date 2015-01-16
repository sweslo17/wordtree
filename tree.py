from node import node
tree = node("grandmother", [
		node("daughter", [
			node("granddaughter"),
			node("grandson")]),
		node("son", [
			node("granddaughter"),
			node("grandson")])
		])
#tree.addlist(['xyz','abc'])
tree.addnode('xyz')
temp = tree.search('xyz')
temp.addnode('abc')
print tree
