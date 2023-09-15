"""
The Fibonacci numbers are a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. 
In mathematical terms, the Fibonacci sequence is defined recursively as follows:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

So, the first few Fibonacci numbers are:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
"""

def fibonacci(n):
    if n in (0, 1):
        return n
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)



"""
we can use the <yield> keyword to convert any Python function into a Python generator. 
Yields function similarly to a conventional return keyword. However, it will always return a generator object.
"""
def creating_gen(index):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for i in range(index):
        yield months[i]
        
# create a generator, can use next function to get its values, or use for loop.
next_month = creating_gen(5) 
next(next_month)
for month in next_month:
    print(month)

