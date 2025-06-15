# Utility functions for data conversion and filtering

def get_transactions(products, customers_order):

    for order in customers_order:
        # get the product detials:
        product = products.get(order["product_id"])

        if product:
            # get total amount of buying that product
            expenses = product["price"] * order["quantity"]

            if expenses >= 70:
                print(
                    f"{product["name"]} has a large order of ${expenses:.2f}")


def convert_currency_get_discount(price_usd):
    exchange_rate_from_usd_ngn = 1700
    discount_threshold = 2000.00
    discount_rate = 0.10  # @10% discount

    price_ngn = price_usd * exchange_rate_from_usd_ngn

    final_price = price_ngn
    print(f"\nItem Price (NGN): #{price_ngn:.2f}  ->  Initial Price (USD): ${price_usd:.2f}")


    # Applying conditional discount
    if price_ngn > discount_threshold:
        discount_amount = price_ngn * discount_rate

        final_price = price_ngn - discount_amount
        print(f"  > Item qualifies for a 10% discount!")
        print(f"  > Final discounted price: ${final_price:.2f}")
    
    return final_price
