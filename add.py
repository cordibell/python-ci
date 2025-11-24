def add(x: int, y: int) -> int:
    """Returns the sum of two integers."""
     if not type(x) == int or not type(y) == int:
         raise TypeError("Both arguments must be integers.")
    return x + y

