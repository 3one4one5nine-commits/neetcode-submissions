class MyHashSet:

    def __init__(self):
        self.d={}
        self.count=0
        self.l=[]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.d[key]=self.count
            self.count+=1
            self.l.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.l[self.d.pop(key)]=None

    def contains(self, key: int) -> bool:
        if self.d.get(key)==None:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)