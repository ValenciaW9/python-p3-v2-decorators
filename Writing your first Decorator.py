# To write your first decorator, you'll need to tie all of these concepts together. You will need to write a function that....
# 1. Take a function as an argument.
# 2. Has an inner function defined inside of it.
# 3. Returns he inner function.


def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")

    return wrapper


def get_called():
    print("I am the function and I am being called.")



#We've created a decorator and we've created a function to pass in. All that's left to do is put it all together:
    
get_called = decorator(get_called)
get_called()
# Iam the output that lets you know the function is about to be called.
#I am the function and I am being called.
# I am the output that lets you know the function has been called.

#Python allows us to perform the decoration step in a more decorative fashion with the @ symbil. This is also called "pie syntax"#
#decirator
def get_called()
     print(" O am the  function and I am  being called/")

     get_called()
     # I am the output that let  you know the function is about to be called.")
     # I am  the function and Iam being called.
     # Iam the output that lets you know tge function has been c