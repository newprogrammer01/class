class Number:
    def __init__(self,number):
        self.number=number
    def get_length(self):
        return len(str(self.number))
num=Number(number=12345)
print(num.get_length())