class Number:
    def __init__(self,number):
        self.number=number
    def get_number(self):
        if self.number%1==0:
            return self.number
x=Number(number=100)
print(x.get_number())