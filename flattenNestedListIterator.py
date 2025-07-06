class NestedInteger:
    def __init__(self,value):
        if isinstance(value,int):
            self._integer=value
            self._list=None
        else:
            self._integer=None
            self._list=[NestedInteger(x) for x in value]

    def isInteger(self):
        return self._integer is not None
    
    def getInteger(self):
        return self._integer
    
    def getList(self):
        return self._list

class NestedIterator:
    def __init__(self,nestedList):
        self.stack=[]
        self._prepare_stack(nestedList)

    def _prepare_stack(self,nestedList):
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        return self.stack.pop().getInteger()
                    
    def hasNext(self):
        while self.stack:
            top=self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self._prepare_stack(top.getList())
        return False
                    

nestedList = [NestedInteger([1,1]),NestedInteger(2),NestedInteger([1,1])]
iterator=NestedIterator(nestedList)

res=[]
while iterator.hasNext():
    res.append(iterator.next())

print(res)