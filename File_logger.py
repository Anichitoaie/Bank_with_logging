import inspect
import logging
import traceback

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

def get_function_parameters_and_values():
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    return ([(i, values[i]) for i in args])

def add(a,b):
    sum=a+b
    logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
    return sum


a=int(input())
b=int(input())

logging.basicConfig(filename='example.log', level=logging.DEBUG,format='%(asctime)s-> %(message)s',
                            datefmt='%m-%d-%Y %H:%M:%S')

logging.debug(add(a,b))
