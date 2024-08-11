from functools import reduce
from typing import Any, Callable

type Composable = Callable[[Any], Any]

def compose(*functions: Composable) -> Composable:
  def apply(value: Any, fn: Composable) -> Any:
      return fn(value)
  return lambda data: reduce(apply, functions, data)

def func_a(data: Any) ->  Any:
  pass

def func_b(data: Any) ->  Any:
  pass

result = compose(func_a, func_b)(data)
