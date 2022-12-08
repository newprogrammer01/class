class Number:
    def __init__(self,number):
        self.number=number
    def is_even(self):
        if self.number%1==0 and self.number%2==0:
            return True
        if self.number%1==0 and self.number%2==0:
            return False
x=Number(number=1048)
print(x.is_even())