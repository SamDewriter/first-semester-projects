# Utility functions for data conversion and filtering
import json
from typing import Dict, List, Tuple

def convert_currency(price: float, exchange_rate: float) -> float:
    "Convert product price to another currency"
    return round(price * exchange_rate, 2)

def apply_discount(price: float, quantity: int) -> float:
    "Apply conditional discount based on quantity"
    if quantity > 10:
        return price * 0.9  # 10% discount for bulk orders
    elif quantity > 5:
        return price * 0.95  # 5% discount for medium orders
    return price

def flag_large_orders(orders: List[Dict], threshold: float = 500) -> List[Dict]:
    "Flag orders with total amount exceeding threshold"
    for order in orders:
        order['is_large_order'] = order['total'] > threshold
    return orders

def save_to_json(data: Dict, filename: str) -> None:
    "Saving report data to JSON file"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)