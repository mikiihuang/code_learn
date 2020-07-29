__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-28

def decorator(func):
    def wrapper(*args,**kargs):
        print(func.__name__)
        return func(*args,**kargs)
    return wrapper