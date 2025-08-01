def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.
    
    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
    - The result of the operation, or a specific message for division by zero or invalid operation
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
