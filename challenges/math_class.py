"""
Implement a math class with methods for addition, subtraction,
multiplication and division. If an input is provided that is not an
int, a message should be returned instead of raising an error.

    'a' + 3  # should return 'Inputs must be numbers!'

"""


class Math:
        
    def add(self, x, y):
        if str(x).isnumeric() and str(y).isnumeric():
            return (x + y)
        else:
            return 'Inputs must be numbers!'
    
    def subtract(self, x, y):
        if str(x).isnumeric() and str(y).isnumeric():
            return (x - y)
        else:
            return 'Inputs must be numbers!'
    
    def multiply(self, x, y):
        if str(x).isnumeric() and str(y).isnumeric():
            return (x * y)
        else:
            return 'Inputs must be numbers!'
    
    def divide(self, x, y):
        if str(x).isnumeric() and str(y).isnumeric():
            return (x/y)
        else:
            return 'Inputs must be numbers!'
    

