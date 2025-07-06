class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self,capacity):
        self.cache={}
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def _remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    def _add_to_front(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    def get(self,key):
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1
    def put(self,key,value):
        if key in self.cache:
            self._remove(self.cache[key])
        node=Node(key,value)
        self._add_to_front(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

commands=["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

obj=None
res=[]

for cmd,arg in zip(commands,args):
    if cmd =="LRUCache":
        obj=LRUCache(*arg)
        res.append(None)
    elif cmd =="put":
        obj.put(*arg)
        res.append(None)
    elif cmd =="get":
        output=obj.get(*arg)
        res.append(output)

print(res)