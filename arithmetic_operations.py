def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs arithmetic operations (add, subtract, multiply, divide) on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation type ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float: Result of the operation
    
    Raises:
        ValueError: If operation is invalid or division by zero occurs
    """
    operation = operation.lower().strip()  # Normalize input
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError(f"Invalid operation: '{operation}'. Must be 'add', 'subtract', 'multiply', or 'divide'")