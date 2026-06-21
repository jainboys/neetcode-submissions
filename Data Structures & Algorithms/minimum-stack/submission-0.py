class MinStack:

    def __init__(self):
        self.lst = []
        self.mlst = []
        

    def push(self, val: int) -> None:
        self.lst.append(val)
        if not self.mlst:
            self.mlst.append(val)
        else:
            self.mlst.append(min(self.mlst[-1], val))

    def pop(self) -> None:
        self.mlst.pop()
        return self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.mlst[-1]
        
