# Python Technical Interview Quesions/Solutions


## Question 1

	Given two strings `s` and `t`, determine whether some anagram of `t` is a substring of `s`. For example: if `s = "udacity"` and `t = "ad"`, then the function returns `True`. Your function definition should look like: `question1(s, t)` and return a boolean `True` or `False`.

	Solution Details:

		My Solution uses a list datastructure, since the input data is 2 dimenstional and not related. First I put all the permutaions of t in a list, then I loop through the list until I find a match. This is the brute force, or naive approach.

		Runtime => O(n^2 + 1)


## Question 2

	Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

	Solution Details:

		My solutions runs 2 loops checking each string combination for the longest palindrome, and updates the stored palindrome if a longer one is found. This is the brute force, or naive approach.

		Runtime => 0(n^3)


## Question 3

	Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
	{'A': [('B', 2)],
	 'B': [('A', 2), ('C', 5)], 
	 'C': [('B', 5)]}
	Vertices are represented as unique strings. The function definition should be question3(G)

	Solution Details:

		My solution uses Kruskel's algorithm: it takes the input graph, an creates a set list from the graph in the format
		(Vertex, Edge, Weight), then sorts the set list, and adds the edge to a new graph one by one, checking if the 
		added edge makes a cycle, and if it does, removing it.

		Runtime => O(ElogE) or O(ElogV)


## Question 4

	Find the least common ancestor between two nodes on a binary search tree.
	The least common ancestor is the farthest node from the root that is an ancestor
	of both nodes. For example, the root is a common ancestor of all nodes on the
	tree, but if both nodes are descendents of the root's left child, then that left
	child might be the lowest common ancestor. You can assume that both nodes are in
	the tree, and the tree itself adheres to all BST properties. The function
	definition should look like question4(T, r, n1, n2), where Tis the tree
	represented as a matrix, where the index of the list is equal to the integer
	stored in that node and a 1 represents a child node, r is a non-negative integer
	representing the root, and n1 and n2 are non-negative integers representing the
	two nodes in no particular order. For example, one test case might be ...

	question4([[0, 1, 0, 0, 0],
	         [0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0],
	         [1, 0, 0, 0, 1],
	         [0, 0, 0, 0, 0]],
	        3,
	        1,
	        4)

	Solution Details:

		My solution finds the path from the root to node_1 and stores it in an array, 
		then, while node_2 does not equal the root, it moves up the tree until it finds a matching parent
		within the node_1 array.

		Runtime => O(n)


## Question 5

	Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

	class Node(object):
	  def __init__(self, data):
	    self.data = data
	    self.next = None

	Solution Details:

		My solution takes in a linked list, defined by the head of the list, since all other nodes can be gathered
		from the head, and the number that is m elements from the end. The function goes back each node in the list m number of times, and returns the value of that node.

		Runtime => 0(n) where n is m