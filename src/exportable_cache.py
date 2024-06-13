import os
import pickle
from functools import wraps
from typing import Callable, ParamSpec, TypeVar, NewType

Param = ParamSpec('Param')
ParamT = NewType('ParamT', Param)
RetType = TypeVar('RetType')
FuncType = Callable[[Param], RetType]

def exportable_cache(func: Callable) -> FuncType:
    func.cache = {}
    if os.path.exists("cache.pkl"):
        with open("cache.pkl", 'rb') as f:
            func.cache = pickle.load(f)
    
    @wraps(func)
    def wrapper(*args: ParamT) -> RetType:
        if args in func.cache.keys():
            return func.cache[args]
        else:
            result = func(*args)
            func.cache[args] = result
            return result
        
    return wrapper

def dump_cache(func: Callable) -> None:
    with open("cache.pkl", 'wb') as f:
        pickle.dump(func.cache, f)