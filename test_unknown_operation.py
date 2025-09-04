#!/usr/bin/env python3
"""Test script to verify the unknown operation handling fix"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import calculate

def test_unknown_operation_handling():
    print("Testing unknown operation handling...")
    
    # Test valid operations
    try:
        result = calculate('add', 5, 3)
        print(f"✓ Valid operation 'add' works: 5 + 3 = {result}")
    except Exception as e:
        print(f"✗ Valid operation 'add' failed: {e}")
    
    try:
        result = calculate('multiply', 4, 7)
        print(f"✓ Valid operation 'multiply' works: 4 * 7 = {result}")
    except Exception as e:
        print(f"✗ Valid operation 'multiply' failed: {e}")
    
    # Test unknown operations
    try:
        result = calculate('mod', 10, 3)
        print(f"✗ Unknown operation 'mod' should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Unknown operation 'mod' correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Unknown operation 'mod' raised unexpected error: {e}")
    
    try:
        result = calculate('sqrt', 16, 0)
        print(f"✗ Unknown operation 'sqrt' should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Unknown operation 'sqrt' correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Unknown operation 'sqrt' raised unexpected error: {e}")
    
    try:
        result = calculate('invalid_op', 1, 2)
        print(f"✗ Unknown operation 'invalid_op' should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Unknown operation 'invalid_op' correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Unknown operation 'invalid_op' raised unexpected error: {e}")
    
    # Test empty string operation
    try:
        result = calculate('', 1, 2)
        print(f"✗ Empty operation should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Empty operation correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Empty operation raised unexpected error: {e}")

if __name__ == "__main__":
    test_unknown_operation_handling()
