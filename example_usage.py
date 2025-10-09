"""
Example usage of Keanu's Candy Store system.

This file demonstrates how to use the various classes in the candy store system.
"""

from keanus_candy.system_model import (
    User, Staff, Candy, Catalog, ShoppingCart, 
    Order, CreditCard, PayPal
)


def main():
    """Demonstrate the candy store system functionality."""
    
    # Create some candies
    chocolate_bar = Candy(1, "Chocolate Bar", 2.99, 50, "Milk Chocolate")
    gummy_bears = Candy(2, "Gummy Bears", 1.99, 100, "Mixed Fruit")
    lollipop = Candy(3, "Lollipop", 0.99, 75, "Cherry")
    
    # Create catalog and add candies
    catalog = Catalog()
    catalog.add_candy(chocolate_bar)
    catalog.add_candy(gummy_bears)
    catalog.add_candy(lollipop)
    
    # Create a user
    user = User(1, "John Doe", "john@example.com", "password123")
    
    # User adds items to cart
    user.add_to_cart(chocolate_bar, 2)
    user.add_to_cart(gummy_bears, 1)
    user.add_to_cart(lollipop, 3)
    
    # Display cart contents
    print("Shopping Cart Contents:")
    for item in user.cart.items:
        print(f"  {item.candy.name} x{item.quantity} = ${item.subtotal():.2f}")
    print(f"Total: ${user.cart.calculate_total():.2f}")
    
    # Checkout with credit card
    credit_card = CreditCard("1234567890123456", "John Doe")
    order = user.checkout("Credit Card")
    
    print(f"\nOrder #{order.order_id} created:")
    print(f"Total: ${order.total_amount:.2f}")
    print(f"Payment Method: {order.payment_method}")
    print(f"Status: {order.status}")
    
    # Create a staff member
    staff = Staff(2, "Jane Smith", "jane@candystore.com", "staff123", "Manager")
    
    # Staff updates inventory
    staff.update_inventory(chocolate_bar, 45)  # Reduced from 50 to 45
    print(f"\nInventory updated. Chocolate bars now in stock: {chocolate_bar.quantity}")
    
    # Staff views sales report
    sales_report = staff.view_sales_report([order])
    print(f"Sales Report: {sales_report}")


if __name__ == "__main__":
    main()
