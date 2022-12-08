class Number:
    def __init__(self,number):
        self.number=number
    def is_odd(self):
        if self.number%2==0:
            return False
        if self.number%2==1:
            return True
y=Number(number=10)
print(y.is_odd())