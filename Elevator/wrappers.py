from inspect import signature, getfullargspec, getargvalues

def printlog(func):
    def printlog_wrapper(*args, **kwargs):

        print(func)
        # print('func name is:', func.__repr__)
        # print('function arguments are:', args, kwargs)
        print('function signature is:', getfullargspec(func)[0])
        print('values passed to args:', locals()['args'])
        print('values passed to kwargs:', locals()['kwargs'])
        # print('positional arguments are:', signature(func)[0:2])
        func(*args, **kwargs)

    return printlog_wrapper


class LogWrappedFunction(object):
    def __init__(self, function):
        self.function = function

    def logAndCall(self, *arguments, **namedArguments):
        print(f"Calling {self.function.__name__} with arguments {arguments} and named arguments {namedArguments}")
        self.function.__call__(*arguments, **namedArguments)


def logwrap(function):
    return LogWrappedFunction(function).logAndCall
