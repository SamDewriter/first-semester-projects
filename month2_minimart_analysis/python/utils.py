# Utility functions for data conversion and filtering

def convert_currency(amount_usd, rate=0.85):
    """Convert USD to another currency (e.g., EUR at 0.85 rate)."""
    return round(amount_usd * rate, 2)

def apply_discount(price, threshold=100, discount_rate=0.10):
    """Apply discount if price exceeds threshold."""
    if price > threshold:
        return round(price * (1 - discount_rate), 2)
    return price

def print_newline():
    """
    Print a newline for better readability.
    """
    print("--------------------------------------------------")
    print("\n")  # Print a newline for spacing
    pass