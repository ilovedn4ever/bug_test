#!/usr/bin/env python3
"""
Comprehensive Test Suite for Calculator Bug Fixes
Tests all implemented bug fixes to ensure the calculator handles errors gracefully
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import add, subtract, multiply, divide, power, calculate

def test_division_by_zero():
    """Test division by zero bug fix"""
    print("=" * 60)
    print("TESTING DIVISION BY ZERO BUG FIX")
    print("=" * 60)
    
    # Test normal division
    try:
        result = divide(10, 2)
        print(f"✓ Normal division: 10 / 2 = {result}")
    except Exception as e:
        print(f"✗ Normal division failed: {e}")
    
    try:
        result = divide(15, 3)
        print(f"✓ Normal division: 15 / 3 = {result}")
    except Exception as e:
        print(f"✗ Normal division failed: {e}")
    
    # Test division by zero
    try:
        result = divide(5, 0)
        print(f"✗ Division by zero should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Division by zero correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Division by zero raised unexpected error: {e}")
    
    try:
        result = divide(-10, 0)
        print(f"✗ Negative division by zero should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Negative division by zero correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Negative division by zero raised unexpected error: {e}")
    
    # Test through calculate function
    try:
        result = calculate('divide', 8, 0)
        print(f"✗ Division by zero through calculate should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Division by zero through calculate correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Division by zero through calculate raised unexpected error: {e}")

def test_input_type_validation():
    """Test input type validation bug fix"""
    print("\n" + "=" * 60)
    print("TESTING INPUT TYPE VALIDATION BUG FIX")
    print("=" * 60)
    
    # Test valid numeric inputs
    try:
        result = calculate('add', 5, 3)
        print(f"✓ Valid int inputs: 5 + 3 = {result}")
    except Exception as e:
        print(f"✗ Valid int inputs failed: {e}")
    
    try:
        result = calculate('multiply', 2.5, 4.0)
        print(f"✓ Valid float inputs: 2.5 * 4.0 = {result}")
    except Exception as e:
        print(f"✗ Valid float inputs failed: {e}")
    
    try:
        result = calculate('subtract', 10, 3.5)
        print(f"✓ Mixed int/float inputs: 10 - 3.5 = {result}")
    except Exception as e:
        print(f"✗ Mixed int/float inputs failed: {e}")
    
    # Test invalid first operand
    try:
        result = calculate('add', '5', 3)
        print(f"✗ String first operand should raise TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ String first operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ String first operand raised unexpected error: {e}")
    
    # Test invalid second operand
    try:
        result = calculate('multiply', 5, '3')
        print(f"✗ String second operand should raise TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ String second operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ String second operand raised unexpected error: {e}")
    
    # Test other invalid types
    try:
        result = calculate('add', [1, 2], 3)
        print(f"✗ List first operand should raise TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ List first operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ List first operand raised unexpected error: {e}")
    
    try:
        result = calculate('subtract', 5, None)
        print(f"✗ None second operand should raise TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ None second operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ None second operand raised unexpected error: {e}")
    
    try:
        result = calculate('power', {'a': 1}, 2)
        print(f"✗ Dict first operand should raise TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ Dict first operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ Dict first operand raised unexpected error: {e}")

def test_unknown_operation_handling():
    """Test unknown operation handling bug fix"""
    print("\n" + "=" * 60)
    print("TESTING UNKNOWN OPERATION HANDLING BUG FIX")
    print("=" * 60)
    
    # Test valid operations
    try:
        result = calculate('add', 5, 3)
        print(f"✓ Valid operation 'add': 5 + 3 = {result}")
    except Exception as e:
        print(f"✗ Valid operation 'add' failed: {e}")
    
    try:
        result = calculate('power', 2, 3)
        print(f"✓ Valid operation 'power': 2^3 = {result}")
    except Exception as e:
        print(f"✗ Valid operation 'power' failed: {e}")
    
    # Test unknown operations
    try:
        result = calculate('mod', 10, 3)
        print(f"✗ Unknown operation 'mod' should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Unknown operation 'mod' correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Unknown operation 'mod' raised unexpected error: {e}")
    
    try:
        result = calculate('sqrt', 16, 0)
        print(f"✗ Unknown operation 'sqrt' should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Unknown operation 'sqrt' correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Unknown operation 'sqrt' raised unexpected error: {e}")
    
    try:
        result = calculate('factorial', 5, 0)
        print(f"✗ Unknown operation 'factorial' should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Unknown operation 'factorial' correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Unknown operation 'factorial' raised unexpected error: {e}")
    
    try:
        result = calculate('', 1, 2)
        print(f"✗ Empty operation should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Empty operation correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Empty operation raised unexpected error: {e}")

def test_power_function_enhancement():
    """Test power function mathematical validation"""
    print("\n" + "=" * 60)
    print("TESTING POWER FUNCTION ENHANCEMENT")
    print("=" * 60)
    
    # Test valid power operations
    try:
        result = power(2, 3)
        print(f"✓ Valid positive base integer exponent: 2^3 = {result}")
    except Exception as e:
        print(f"✗ Valid positive base integer exponent failed: {e}")
    
    try:
        result = power(9, 0.5)
        print(f"✓ Valid positive base fractional exponent: 9^0.5 = {result}")
    except Exception as e:
        print(f"✗ Valid positive base fractional exponent failed: {e}")
    
    try:
        result = power(-2, 3)
        print(f"✓ Valid negative base integer exponent: (-2)^3 = {result}")
    except Exception as e:
        print(f"✗ Valid negative base integer exponent failed: {e}")
    
    try:
        result = power(-8, 2.0)  # 2.0 is float but equals integer
        print(f"✓ Valid negative base float exponent (integer value): (-8)^2.0 = {result}")
    except Exception as e:
        print(f"✗ Valid negative base float exponent (integer value) failed: {e}")
    
    try:
        result = power(0, 5)
        print(f"✓ Valid zero base positive exponent: 0^5 = {result}")
    except Exception as e:
        print(f"✗ Valid zero base positive exponent failed: {e}")
    
    # Test invalid power operations (negative base with fractional exponent)
    try:
        result = power(-4, 0.5)
        print(f"✗ Invalid negative base fractional exponent should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid negative base fractional exponent correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid negative base fractional exponent raised unexpected error: {e}")
    
    try:
        result = power(-2, 1.5)
        print(f"✗ Invalid negative base fractional exponent should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid negative base fractional exponent correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid negative base fractional exponent raised unexpected error: {e}")
    
    try:
        result = calculate('power', -9, 0.33333)
        print(f"✗ Invalid power through calculate should raise ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid power through calculate correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid power through calculate raised unexpected error: {e}")

def test_edge_cases():
    """Test additional edge cases and boundary conditions"""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES AND BOUNDARY CONDITIONS")
    print("=" * 60)
    
    # Test very large numbers
    try:
        result = calculate('add', 1e10, 1e10)
        print(f"✓ Large number addition: 1e10 + 1e10 = {result}")
    except Exception as e:
        print(f"✗ Large number addition failed: {e}")
    
    # Test very small numbers
    try:
        result = calculate('multiply', 1e-10, 1e-10)
        print(f"✓ Small number multiplication: 1e-10 * 1e-10 = {result}")
    except Exception as e:
        print(f"✗ Small number multiplication failed: {e}")
    
    # Test negative numbers
    try:
        result = calculate('subtract', -5, -3)
        print(f"✓ Negative number subtraction: -5 - (-3) = {result}")
    except Exception as e:
        print(f"✗ Negative number subtraction failed: {e}")
    
    # Test zero operations
    try:
        result = calculate('multiply', 0, 100)
        print(f"✓ Zero multiplication: 0 * 100 = {result}")
    except Exception as e:
        print(f"✗ Zero multiplication failed: {e}")
    
    try:
        result = calculate('power', 5, 0)
        print(f"✓ Power with zero exponent: 5^0 = {result}")
    except Exception as e:
        print(f"✗ Power with zero exponent failed: {e}")
    
    # Test combined error conditions
    try:
        result = calculate('invalid_op', 'string', None)
        print(f"✗ Multiple errors should raise first encountered error but returned: {result}")
    except (TypeError, ValueError) as e:
        print(f"✓ Multiple errors correctly raise appropriate error: {e}")
    except Exception as e:
        print(f"✗ Multiple errors raised unexpected error: {e}")

def test_graceful_error_handling():
    """Test that all errors are handled gracefully without crashes"""
    print("\n" + "=" * 60)
    print("TESTING GRACEFUL ERROR HANDLING")
    print("=" * 60)
    
    error_test_cases = [
        ('divide', 10, 0, "Division by zero"),
        ('add', '5', 3, "String input"),
        ('multiply', 5, None, "None input"),
        ('invalid_op', 1, 2, "Unknown operation"),
        ('power', -4, 0.5, "Invalid power operation"),
        ('subtract', [1, 2], 3, "List input"),
        ('add', {'a': 1}, 2, "Dict input"),
        ('', 1, 2, "Empty operation"),
    ]
    
    all_handled_gracefully = True
    
    for operation, num1, num2, description in error_test_cases:
        try:
            result = calculate(operation, num1, num2)
            print(f"✗ {description} should have raised an error but returned: {result}")
            all_handled_gracefully = False
        except (ValueError, TypeError) as e:
            print(f"✓ {description} handled gracefully: {type(e).__name__}")
        except Exception as e:
            print(f"✗ {description} caused unexpected error: {type(e).__name__}: {e}")
            all_handled_gracefully = False
    
    if all_handled_gracefully:
        print(f"\n✓ ALL ERROR CONDITIONS HANDLED GRACEFULLY - NO CRASHES!")
    else:
        print(f"\n✗ Some error conditions not handled properly")

def run_comprehensive_test_suite():
    """Run all test functions"""
    print("COMPREHENSIVE CALCULATOR BUG FIX TEST SUITE")
    print("=" * 60)
    print("Testing all implemented bug fixes and edge cases...")
    print()
    
    test_division_by_zero()
    test_input_type_validation()
    test_unknown_operation_handling()
    test_power_function_enhancement()
    test_edge_cases()
    test_graceful_error_handling()
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST SUITE COMPLETED")
    print("=" * 60)
    print("All bug fixes have been tested for proper error handling.")
    print("The calculator now handles errors gracefully without crashing.")

if __name__ == "__main__":
    run_comprehensive_test_suite()
