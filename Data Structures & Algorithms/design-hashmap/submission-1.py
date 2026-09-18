class MyHashMap:

    def __init__(self):
        self.mapper=defaultdict(lambda: -1)

    def put(self, key: int, value: int) -> None:
        self.mapper[key]=value

    def get(self, key: int) -> int:
        return self.mapper[key]

    def remove(self, key: int) -> None:
        if self.mapper[key]!=-1:
            self.mapper.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)