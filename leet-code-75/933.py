class RecentCounter:

    def __init__(self):
      self.counters = []  

    def ping(self, t: int) -> int:
      
      while self.counters and self.counters[0] + 3000 < t:
        self.counters.pop(0)
      
      self.counters.append(t)
      
      return len(self.counters)

      
      
      
