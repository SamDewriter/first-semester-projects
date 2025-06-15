# Utility functions for data conversion and filtering

def convert_currency(amount, rate):
    """
    Converts an amount to a different currency using the provided rate.
    """
    return round(amount * rate, 2)

def apply_discount(amount, threshold=100, discount_rate=0.10):
    """
    Applies discount if amount exceeds threshold.
    """
    if amount > threshold:
        return round(amount * (1 - discount_rate), 2)
    return round(amount, 2)

def format_currency(amount):
    """
    Formats amount as currency string.
    """
    return f"${amount:,.2f}"
