from collections import defaultdict

class MinStack:
    def __init__(self):
        self.array = []
        pass

    def push(self, val: int) -> None:
        if len(self.array) == 0:
            self.array.append([val, val])
        else:
            _, prevMin = self.array[-1]
            self.array.append([val, min(prevMin, val)])

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        top, _ = self.array[-1]
        return top

    def getMin(self) -> int:
        _, curMin = self.array[-1]
        return curMin        
