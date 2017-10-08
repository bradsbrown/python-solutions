"""
	Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

	{'A': [('B', 2)],
	 'B': [('A', 2), ('C', 5)], 
	 'C': [('B', 5)]}
	Vertices are represented as unique strings. The function definition should be question3(G)
"""


from operator import itemgetter

def isCycle(parent, previous, newDict, root):
	print 'parent: ', parent
	for edge in newDict[parent]:
		if edge[0] == root and edge[0] != previous:
			return True
		if edge[0] != previous:
			print 'recursion', edge[0], parent
			return isCycle(edge[0], parent, newDict, root)
	return "no cycle here"

def startCycle(parent, previous, newDict, root):
	for edge in newDict[root]:
		print 'edge: ', edge
		print isCycle(edge[0], root, a, root)

def question3(adjDict):
	newDict = {key: list([]) for key in adjDict.keys()}
	root = None
	edgeList = []

	for vert in adjDict:
		for edge in adjDict[vert]:
			edge = list(edge)
			edge.insert(0, vert)
			edge = tuple(edge)
			edgeList.append(edge)

	list.sort(edgeList, key = itemgetter(2))
	print edgeList, '\n\n'
	root = edgeList[0][0]
	print 'ROOT ', root
	
	for union in edgeList:
		newDict[union[0]].append((union[1], union[2]))
		# print 'is cycle? ', union[1], union[0], root
		print 'newDict ', newDict
		for edge in newDict[root]:
			if isCycle(edge[0], root, newDict, root) == True:
				newDict[union[0]].pop()
		print 'after check ', newDict
	print 'FINAL CHECK', startCycle(edge[0], root, newDict, root)
	return newDict

a = {
	'A': [('B', 3), ('D', 4)],
	'B': [('A', 3), ('E', 4), ('F', 6)],
	'C': [('E', 5)],
	'D': [('A', 4)],
	'E': [('B', 4), ('F', 5), ('C', 5)],
	'F': [('B', 6), ('E', 5)]
}

print question3(a)
# Should return
# { 
#   'A': [('B', 3), ('D', 4)],
#	'B': [('A', 3), ('E', 4)],
#	'C': [('E', 5)],
#	'D': [('A', 4)],
#	'E': [('B', 4), ('C', 5), ('F', 5)],
#	'F': [('E', 5)]
# }




