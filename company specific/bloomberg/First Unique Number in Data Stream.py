'''
Design a data structure that support the following methods:

public class Stream {
    
    public Stream() {
        // do intialization if necessary
    }

	/**
	* Adds integer num to a stream of integers.
	*/
    public void add(int num) {
        // write your code here
    }

	/**
	*  Returns the first unique integer in the stream if found else return null.
	*/
    public Integer getFirstUnique() {
        // write your code here
    }
}
Example:

Stream s = new Stream();
s.add(2);
s.getFirstUnique(); // 2
s.add(2);
s.getFirstUnique(); // null
s.add(3);
s.getFirstUnique(); // 3
s.add(4);
s.getFirstUnique(); // 3
s.add(3);
s.getFirstUnique(); // 4
'''
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    def insert(self, val):
        newNode = Node(val)
        newNode.prev = self.tail.prev 
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.count += 1
        return newNode

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next = nxt
        node.next.prev = prev
        self.count -= 1
    
    def isEmpty(self):
        return (self.count == 0)

class firstUnique:
    def __init__(self):
        self.dll = DLL()
        self.numDict = {}
    
    def insert(self, num):
        if num in self.numDict and self.numDict[num] != -1:
            self.dll.remove(self.numDict[num])
            self.numDict[num] = -1
        else:
            self.numDict[num] = self.dll.insert(num)
    
    def getFirstUniqueInteger(self):
        if self.dll.isEmpty():
            return -1
        return self.dll.head.next.val