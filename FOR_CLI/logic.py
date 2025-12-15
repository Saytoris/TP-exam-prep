def calculate_sum(n):
    """
    Обчислює суму перших n членів арифметичної прогресії: 2, 4, 6...
    Формула: Sn = n * (n + 1)
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    return n * (n + 1)