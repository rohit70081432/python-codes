class MathOperations:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0

obj = MathOperations()
print(obj.add())        
print(obj.add(5))       
print(obj.add(5, 10))  
print(obj.add(5, 10, 15))  
