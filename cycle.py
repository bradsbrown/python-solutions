from operator import itemgetter

def isCycle(parent, previous, a, root):
	# if len(adjDict[parent]) < 1:
	# 	return "no cycle here"
	print 'parent: ', parent
	for edge in a[parent]:
		if edge[0] == root and edge[0] != previous:
			print edge[0], previous
			print 'CYCLE found'
			return True
		if edge[0] != previous:
			print 'recursion: ', edge[0], parent
			return isCycle(edge[0], parent, a, root)

adjDict = {
    'A': [('B', 3), ('D', 4)],
    'B': [('A', 3), ('E', 4), ('F', 6)],
	'C': [('E', 5)],
	'D': [('A', 4)],
	'E': [('B', 4), ('F', 5), ('C', 5)],
	'F': [('E', 5), ('B', 6)]
}

test = {
	'A': [('B', 3), ('D', 4)], 
	'C': [('E', 5)],
	'B': [('A', 3), ('E', 4), ('F', 6)],
	'E': [('B', 4), ('C', 5), ('F', 5)],
	'D': [('A', 4)],
	'F': [('E', 5), ('B', 6)]
}

altDict = {
	'A' : [('B', 1)],
	'B' : [('C', 1)],
	'C' : [('D', 1)],
	'D' : [],
}

a = {
	'A': [('B', 3), ('D', 4)],
	'B': [('A', 3), ('E', 4), ('F', 6)],
	'C': [('E', 5)],
	'D': [('A', 4)],
	'E': [('B', 4), ('F', 5), ('C', 5)],
	'F': [('E', 5), ('B', 6)]
}

root = 'A'
edgeList = []

for edge in test[root]:
	print 'edge: ', edge
	print isCycle(edge[0], root, test, root)
for edge in test['F']:
	print 'edge: ', edge
	print isCycle(edge[0], 'F', test, root)

# for vert in adjDict:
# 	for edge in adjDict[vert]:
# 		edge = list(edge)
# 		edge.insert(0, vert)
# 		edge = tuple(edge)
# 		edgeList.append(edge)
# list.sort(edgeList, key=itemgetter(2))
# print edgeList
# print adjDict


