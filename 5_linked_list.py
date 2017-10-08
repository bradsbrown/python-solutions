"""
	Question 5
	Find the element in a singly linked list that's m elements from the end.
	For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
	The function definition should look like question5(ll, m), where ll is the first node of a
	linked list and m is the "mth number from the end". You should copy/paste the Node class below
	to use as a representation of a node in the linked list. Return the value of the node at that position.
"""


head = None

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def newNode(data):
    global head
    node = Node(data)
    node.next = head
    head = node

def question5(head, m):
    main = head
    ref = head
    count = 0

    if(head is not None):
        while(count < m ):
            if(ref == None):
                print (m), "is greater than the number of nodes"
                return -1

            ref = ref.next
            count += 1

    while(ref != None):
        main = main.next
        ref = ref.next

    return main.data

# creates linked list and starts question 5
# def createLinkedList_1():
#     global head
#     newNode(2)
#     newNode(8)
#     newNode(15)
#     newNode(4)
#     newNode(40)
#     return question5(head, 4)

# test case
def createLinkedList_2():
    global head
    newNode(2)
    newNode(8)
    newNode(15)
    newNode(4)
    newNode(40)
    return question5(head, 8)



# print createLinkedList_1()
# returns 4

print createLinkedList_2()
# returns number is greater than # of nodes and -1



