class node(object):
	def __init__(self, value, children = []):
		self.value = value
		if len(children) != 0:
			self.children = children
		else:
			self.children = []
	def __repr__(self,level=0):
		ret = '\t'*level + repr(self.value) + '\n'
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret
	def search(self,value):
		#print self.value
		result = None
		if self.value == value:
			#print "found"
			result = self
			return result
		else:
			for index in range(0,len(self.children)):
				result = self.children[index].search(value)
				if result is not None:
					break
		return result
	def addnode(self,value):
		self.children.append(node(value,[]))
		return self.children[-1]
	def addlist(self,value):
		print value
		'''if len(value) == 1:
			self.addnode(node(value[0]))
			return
		else:
			print self.search(value[0])
			if self.search(value[0]) == None:
				self.addnode(node(value[0]))
			print self.addnode(node(value[0])).search(value[0])
		self.search(value[0]).addlist(value[1:])'''
