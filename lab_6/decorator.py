import time
def method_decorator(method):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        method(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Execution of method {method.__name__}: {execution_time}')
    return wrapper