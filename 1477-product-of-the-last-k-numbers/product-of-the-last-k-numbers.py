class ProductOfNumbers:

    def __init__(self):
        self.stack = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.stack.clear()
            self.stack.append(1)
        else:
            self.stack.append(self.stack[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.stack) - 1
        if k > n:
            return 0
        return self.stack[-1] // self.stack[len(self.stack) - 1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
