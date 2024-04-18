class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end="-->")
        curr = curr.next
    print()

def insertNodeAtHeadofLinkedList(head, ele):
    newBlock = Node(ele)
    newBlock.next = head
    return newBlock

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None
for ele in l:
    head = insertNodeAtHeadofLinkedList(head, ele)
printLinkedList(head)
