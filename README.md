# Supermarket Checkout

## Description
This project implements a supermarket checkout process that calculates the total price of items added to the cart by the customer. It accepts items in any order and applies discounts based on special offers.

## Installation
1. Clone the repository:
    ```
    git clone <repository_url>
    cd supermarket_checkout
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
1. Import the `Checkout` class from `src/checkout.py` and use it to scan items and calculate the total price.
2. Example usage:
    ```python
    from supermarket_checkout.src.checkout import Checkout

    checkout = Checkout()
    checkout.scan("A")
    checkout.scan("B")
    checkout.scan("A")
    total_price = checkout.calculate_total()
    print(total_price)  # Output should be 130
    ```

## Testing
To run the tests, navigate to the project directory and execute:
