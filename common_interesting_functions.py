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


"""
# replace a character in a string text without using .replace() function
"""
def replace_str(text, old, new):
    result = ""
    for s in text:
        if s == old:
            s = new
        result += s
    return result

text = "D t C mpBl ckFrid yS le"
old = " "
new = "a"

replace_str(text, old, new)

# Use .replace() function
text = "D t C mpBl ckFrid yS le"
text.replace(old, new)


"""
Given a positive integer num, write a function that returns True if num is a perfect square else False.
"""
def perfect_square(num):
    num_sqrt = int(num**0.5)
    result = num == num_sqrt**2
    return result

perfect_square(25)
perfect_square(10)


"""
without using any package
Given an integer n, return the number of trailing zeroes in n factorial n!
"""
def factorial_training_zeros(n):
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1

    count = 0
    for s in str(fact)[::-1]:
        if s == "0":
            count += 1
        else:
            break
    return count



"""
You are provided with a large string and a dictionary of the words. 
You have to find if the input string can be segmented into words using the dictionary or not.
"""

def word_segmentation(word, dictionary):

    for i in range(1, len(word)+1):
        word1 = word[0:i]
        if word1 in dictionary:
            word2 = word[i:]
            if (word2 in dictionary) \
                    or (not word2) \
                    or word_segmentation(word2, dictionary):
                return True
    return False

w1 = "shank3cancauseautism"
w2 = "shank3cannotcauseautism"
dictionary = ["shank3", "can", "cause", "autism", "cam", "lack"]

word_segmentation(w1, dictionary)

"""
remove duplicates from a list or array
"""
list1 = [1,1,2,3,3]
list2 = [1,1,1,2,2,2,3,3,4,5,6,7,8]
list(set(list1))
