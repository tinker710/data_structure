class Node:
    def __init__(self,val, p= None ):
        self.val = val
        self.next = p

    def get_val(self):
        return self.val

class NodeList:
    def __init__(self, head=Node(0)):
        self.head = head

    def append(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            p=self.head
            while p.next:
                p=p.next:
            q = Node(val)
            p.next = q

    def insert(self, index, val):
        p=self.head
        if not p:
            return
        j=0
        while j < index and p.next:
            q=p
            p=p.next
            j +=1
        if j < index-1:
            return
        else:
            item = Node(val, p.next)
            p.next = item

    def delete(self, index):
        p = self.head
        if not p:
            return
        j=0
        while j < index and p.next:
            q=p
            p=p.next
            j += 1
        if j < index:
            return
        else:
            q.next = p.next

    def getnode(self, index):
        p=self.head
        j=0
        while j< index and p:
            p = p.next
            j += 1
        return p.val

    def clear_list(self):
        self.head = None
        return
