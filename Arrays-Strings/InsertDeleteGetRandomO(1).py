import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            i = self.map.pop(val)
            self.values[i] = self.values[len(self.values)-1]
            self.values.pop()
            if i < len(self.values):
                self.map[self.values[i]] = i
            return True
        return False

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.values)-1)
        return self.values[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
