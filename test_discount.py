import os
import sys

def test_discount_logic():
    # DEBUG: Let's see what Jenkins is actually sending
    secret = os.getenv('DISCOUNT_CODE')
    print(f"DEBUG: The secret Jenkins sent is: {secret}")
    
    # Let's say we expect the discount to result in 80
    price = 100
    # Dummy logic to check what's happening
    if secret == "SAVE20":
        result = price * 0.8
    else:
        result = price
        
    print(f"DEBUG: Calculated result is: {result}")
    
    assert result == 80.0, "FAILED: Discount was not applied!"

if __name__ == "__main__":
    try:
        test_discount_logic()
    except AssertionError as e:
        print(f"STOP! {e}")
        sys.exit(1) # Force Jenkins to turn RED
