#!/usr/bin/env python3
"""Test script to verify the power function enhancement"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import power, calculate

def test_power_function_enhancement():
    print("Testing power function enhancement...")
    
    # Test valid power operations
    try:
        result = power(2, 3)
        print(f"✓ Valid positive base integer exponent works: 2^3 = {result}")
    except Exception as e:
        print(f"✗ Valid positive base integer exponent failed: {e}")
    
    try:
        result = power(4, 0.5)
        print(f"✓ Valid positive base fractional exponent works: 4^0.5 = {result}")
    except Exception as e:
        print(f"✗ Valid positive base fractional exponent failed: {e}")
    
    try:
        result = power(-2, 3)
        print(f"✓ Valid negative base integer exponent works: (-2)^3 = {result}")
    except Exception as e:
        print(f"✗ Valid negative base integer exponent failed: {e}")
    
    try:
        result = power(-8, 2.0)  # 2.0 is float but equals integer
        print(f"✓ Valid negative base float exponent (integer value) works: (-8)^2.0 = {result}")
    except Exception as e:
        print(f"✗ Valid negative base float exponent (integer value) failed: {e}")
    
    # Test invalid power operations (negative base with fractional exponent)
    try:
        result = power(-4, 0.5)
        print(f"✗ Invalid negative base fractional exponent should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid negative base fractional exponent correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid negative base fractional exponent raised unexpected error: {e}")
    
    try:
        result = power(-2, 1.5)
        print(f"✗ Invalid negative base fractional exponent should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid negative base fractional exponent correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid negative base fractional exponent raised unexpected error: {e}")
    
    try:
        result = power(-9, 0.33333)
        print(f"✗ Invalid negative base fractional exponent should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid negative base fractional exponent correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid negative base fractional exponent raised unexpected error: {e}")
    
    # Test through calculate function
    try:
        result = calculate('power', -4, 0.5)
        print(f"✗ Invalid power through calculate should have raised ValueError but returned: {result}")
    except ValueError as e:
        print(f"✓ Invalid power through calculate correctly raises ValueError: {e}")
    except Exception as e:
        print(f"✗ Invalid power through calculate raised unexpected error: {e}")

if __name__ == "__main__":
    test_power_function_enhancement()
