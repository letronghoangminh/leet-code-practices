class SmallestInfiniteSet:

    def __init__(self):
        self.freq = [True] * 1001

    def popSmallest(self) -> int:
        item = self.freq.index(True)
        self.freq[item] = False

        return item + 1

    def addBack(self, num: int) -> None:
        if not self.freq[num - 1]:
          self.freq[num - 1] = True
