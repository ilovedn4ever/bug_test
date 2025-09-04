#!/usr/bin/env python3
"""Test script to verify the division by zero fix"""

# Import the functions from calculator.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import divide

def test_division_fix():
    print("Testing division by zero fix...")
    
    # Test normal division
    try:
        result = divide(10, 2)
        print(f"✓ Normal division works: 10 / 2 = {result}")
    except Exception as e:
        print(f"✗ Normal division failed: {e}")
    
    # Test division by zero
    try:
        result = divide(5, 0)
        print(f"✗ Division by zero should have raised an error but returned: {result}")
    except ValueError as e:
        print(f"✓ Division by zero correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Division by zero raised unexpected error: {e}")

if __name__ == "__main__":
    test_division_fix()
