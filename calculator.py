def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def power(a, b):
    # Validate mathematically invalid operations
    if a < 0 and isinstance(b, float) and b != int(b):
        raise ValueError(f"Cannot compute fractional power of negative number: ({a})^{b} has no real solution")
    return a ** b

def calculate(operation, num1, num2):
    # Input type validation
    if not isinstance(num1, (int, float)):
        raise TypeError(f"First operand must be a number (int or float), got {type(num1).__name__}")
    if not isinstance(num2, (int, float)):
        raise TypeError(f"Second operand must be a number (int or float), got {type(num2).__name__}")
    
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power
    }
    
    # Check if operation exists before accessing
    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'. Supported operations are: {', '.join(operations.keys())}")
    
    return operations[operation](num1, num2)

if __name__ == "__main__":
    # 测试用例（部分会触发bug）
    print("加法测试:", calculate('add', 5, 3))  # 正常
    print("减法测试:", calculate('subtract', 10, 4))  # 正常
    print("乘法测试:", calculate('multiply', 7, 2))  # 正常
    print("除法测试（正常）:", calculate('divide', 8, 2))  # 正常
    print("除法测试（除零）:", calculate('divide', 5, 0))  # 触发Bug 1
    print("幂运算测试（正常）:", calculate('power', 2, 3))  # 正常
    print("幂运算测试（异常）:", calculate('power', -4, 0.5))  # 触发Bug 2
    print("类型错误测试:", calculate('add', '5', 3))  # 触发Bug 3
    print("未知操作测试:", calculate('mod', 10, 3))  # 触发Bug 4
    




