#!/usr/bin/env python3
"""Test script to verify the input type validation fix"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import calculate

def test_type_validation():
    print("Testing input type validation...")
    
    # Test valid numeric inputs
    try:
        result = calculate('add', 5, 3)
        print(f"✓ Valid int inputs work: 5 + 3 = {result}")
    except Exception as e:
        print(f"✗ Valid int inputs failed: {e}")
    
    try:
        result = calculate('multiply', 2.5, 4.0)
        print(f"✓ Valid float inputs work: 2.5 * 4.0 = {result}")
    except Exception as e:
        print(f"✗ Valid float inputs failed: {e}")
    
    try:
        result = calculate('subtract', 10, 3.5)
        print(f"✓ Mixed int/float inputs work: 10 - 3.5 = {result}")
    except Exception as e:
        print(f"✗ Mixed int/float inputs failed: {e}")
    
    # Test invalid first operand
    try:
        result = calculate('add', '5', 3)
        print(f"✗ String first operand should have raised TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ String first operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ String first operand raised unexpected error: {e}")
    
    # Test invalid second operand
    try:
        result = calculate('add', 5, '3')
        print(f"✗ String second operand should have raised TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ String second operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ String second operand raised unexpected error: {e}")
    
    # Test other invalid types
    try:
        result = calculate('add', [1, 2], 3)
        print(f"✗ List first operand should have raised TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ List first operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ List first operand raised unexpected error: {e}")
    
    try:
        result = calculate('add', 5, None)
        print(f"✗ None second operand should have raised TypeError but returned: {result}")
    except TypeError as e:
        print(f"✓ None second operand correctly raises TypeError: {e}")
    except Exception as e:
        print(f"✗ None second operand raised unexpected error: {e}")

if __name__ == "__main__":
    test_type_validation()
