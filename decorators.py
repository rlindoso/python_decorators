import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        print(f"Posicional args (args): {args}")
        print(f"Nameds args (kwargs): {kwargs}")
        start = time.time()
        print(f"Start time: {start}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"End time: {end}")
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def proccess(param1: int, param2: str):
    time.sleep(param1)
    print(param2)

proccess(param1=1, param2="valor2")
