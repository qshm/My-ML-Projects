from inspect import signature, getfullargspec, getargvalues
from functools import  wraps

def printlog(func):

    @wraps(func)
    def printlog_wrapper(*args, **kwargs):

        print(f'Calling {func.__name__} with signature:{getfullargspec(func)[0]}')
        print('values passed to args:', locals()['args'], 'to kwargs:', list(locals()['kwargs'].values()))
        func(*args, **kwargs)

    return printlog_wrapper

# ----------------------------------------------------------------------------------------------------------------------------------------------------
#another example from stackoverflow
class LogWrappedFunction(object):
    def __init__(self, function):
        self.function = function

    def logAndCall(self, *arguments, **namedArguments):
        print(f"Calling {self.function.__name__} with arguments {arguments} and named arguments {namedArguments}")
        self.function.__call__(*arguments, **namedArguments)


def logwrap(function):
    return LogWrappedFunction(function).logAndCall

