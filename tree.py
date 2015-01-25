from node import node
tree = node("grandmother", [
		node("daughter", [
			node("granddaughter"),
			node("grandson")]),
		node("son", [
			node("granddaughter"),
			node("grandson")]),
		node("abc")
		])
#tree = node('abc',[node('qwe'),node('def')])
#tree.addlist(['xyz','abc'])
#temp_node = tree.search('abc')
#temp_node.addnode('xyz')
temp = tree.search('abc').addnode('xyz')
print tree
