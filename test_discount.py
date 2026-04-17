import os
import discount_service

def test_discount_logic():
    secret = os.getenv('DISCOUNT_CODE')
    
    # Scenario: User uses the correct code
    result = discount_service.apply_discount(100, secret)
    assert result == 80.0, f"Discount failed! Expected 80, got {result}"
    
    # Scenario: User uses a fake code
    result_fake = discount_service.apply_discount(100, "WRONG_CODE")
    assert result_fake == 100, "Logic failed! Wrong code should not give discount."
    
    print("All Discount Tests Passed!")

if __name__ == "__main__":
    test_discount_logic()
