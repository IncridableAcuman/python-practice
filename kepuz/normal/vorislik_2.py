class Number:
    def __init__(self,n):
        self.n=n
    def sum_digit(self):
        return sum(str(self.n))
    