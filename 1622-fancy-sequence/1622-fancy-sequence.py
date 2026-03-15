class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        stored = (val - self.add) % self.MOD
        stored = (stored * inv_mul) % self.MOD
        self.arr.append(stored)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD

        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)