#https://kep.uz/problems/231
class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return Number(self.value + other.value)
    def __sub__(self, other):
        return Number(self.value - other.value)
    def __mul__(self, other):
        return Number(self.value * other.value)
    def __str__(self):
        return str(self.value)