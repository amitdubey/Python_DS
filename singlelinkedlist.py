class Node(object): 
    def __init__(self, data=None, next=None):   
        self.data = data
        self.next_ =next
    def set_data(self,data=None):   
        self.data = data
    def get_data(self,data=None) :    
        return self.data
    def set_next(self, next=None):   
        self.next_ =next
    def get_next(self,next=None) :        
        return self.next_
    def __str__(self,data=None): 
        return str(self.data)
        

                


class LinkedList(object):
    def __init__(self):
        self.head_ = None

    def set_head(self, head_node):
        self.head_ = head_node

    def __len__(self):
        count = 0
        current = self.head_
        while current:
            count += 1
            current = current.get_next()
        return count

    def __str__(self):
        current = self.head_
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output

    # Pops an item from the front of the list
    def pop(self):
        if self.head_:
            self.head_ = self.head_.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    # Returns true if list contains the given value.
    def contains(self, value):
        found = False
        current = self.head_
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    # Deletes all instances of given value in list.
    def delete(self, value):
        current = self.head_
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head_ = current.get_next()
            prev = current
            current = current.get_next()

    # Pushes an item on the front of the list.
    def push(self, value):
        node = Node(value)
        node.set_next(self.head_)
        self.set_head(node)

    def append(self, value):
        node = Node(value)
        current = self.head_
        if not current:
            self.head_ = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)
        
        
def main():
    ll = LinkedList()

    print("Initial size: ", len(ll))
    ll.push(24)
    print("New size: ", len(ll))
    print("List content: ", ll)
    print("Pushing more")
    ll.push(6)
    ll.push(783)
    print("List content: ", ll)
    print("popping...")
    ll.pop()
    print("List content: ", ll)
    print("Does list contain 24?")
    if ll.contains(24):
        print("Yes")
    else:
        print("No")
    print("Deleting 24")
    ll.delete(24)
    print("List content: ", ll)
    print("Pushing another onto end.")
    ll.append(365)
    print("List content: ", ll)


if __name__ == "__main__":
    main()