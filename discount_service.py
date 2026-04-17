import os

def apply_discount(price, code_provided):
    # Fetch the "Official" code from Jenkins environment
    secret_code = os.getenv('DISCOUNT_CODE')
    
    if code_provided == secret_code:
        return price * 0.80  # 20% off
    return price

if __name__ == "__main__":
    # Test it locally with a sample price
    print(f"Final Price for $100: {apply_discount(100, 'SAVE50')}")
