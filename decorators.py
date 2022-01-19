"""
Ref: https://www.w3schools.in/python-tutorial/metaprogramming/


"""
#############################################################
# Import Modules
#############################################################
import logging; logging.basicConfig(level=logging.INFO)
import time
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt



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

# Define Decorator that writes dataframe to file
def write2file(funct):
    # Define inner function that takes any input
    def inner(*args):
        # Call Funct to create dataframe
        logging.info('Function called')
        df = funct(*args)
        df.to_excel('test.xlsx')
        print('Df written to excel')
        # Return that object that has been created
        return df
    # Return the inner function waiting to be executed
    return inner

# Define Second Decorator - Show DataFrame
def tabulate_df(funct):
    def inner(*args):
        logging.info('Function called')
        df = funct(*args)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql')) 
        return df
    return inner

# Decorate Our Function
@write2file
@tabulate_df
def create_df(list1, list2):
    df = pd.DataFrame({'Int':list1, 'String':list2})
    return df

plt.plot([1,2,3,4])
plt.show()
plt.savefig('test.jpeg')








