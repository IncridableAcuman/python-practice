class Shape:
    def __init__(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def area(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            p = (self.a + self.b + self.c) / 2
            s = (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
            return s
        return 0
        