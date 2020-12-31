"""
Ref: https://www.w3schools.in/python-tutorial/metaprogramming/


"""
#############################################################
# Import Modules
#############################################################
import logging; logging.basicConfig(level=logging.INFO)
import time
import pandas as pd


#############################################################
# Example 1
#############################################################

def smart_divide_decorator(func):
    # Define what you want the decorator to do with func 
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if a <= b:     
            # if the condition is met, return the function and execute
            return func(a,b)
        else:
            # Otherwise, return an error message
            print('Error: a < b')
    # Why do we return the inner function here?
    return inner

# Decorate divide
@smart_divide_decorator
def divide(a, b):
    print('Solution => {}'.format(a/b))



#############################################################
# Example 2 - Decorate Print Function 
#############################################################
'''Note: if we do not return the inner function then
    the decorated function is not executed    
'''

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def perct(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@perct
def printer(msg):
    print(msg)



#############################################################
# Example 3 - Write to file 
#############################################################
list1 = [1, 2, 3, 4]
list2 = ['A', 'B', 'C', 'D']

def write2file(funct):
    def inner(*args):
        df = funct(*args)
        df.to_excel('test.xlsx')
        print('Df written to excel')
    return inner

@write2file
def create_df(list1, list2):
    df = pd.DataFrame({'Int':list1, 'String':list2})
    print(df)
    return df

create_df(list1, list2)










