from typing import List, Optional


class Person:
    """Abstract base class for all people in the system."""
    
    def __init__(self, person_id: int, name: str, email: str):
        self.person_id = person_id
        self.name = name
        self.email = email

    def display_info(self):
        return f"{self.name} ({self.email})"


class User(Person):
    """Represents a registered user who can shop."""
    
    def __init__(self, user_id: int, name: str, email: str, password: str):
        super().__init__(user_id, name, email)
        self.password = password
        self.orders: List["Order"] = []
        self.cart: Optional["ShoppingCart"] = None

    def login(self, email: str, password: str) -> bool:
        """Authenticate the user."""
        return self.email == email and self.password == password

    def add_to_cart(self, candy: "Candy", quantity: int):
        """Add candy to shopping cart."""
        if not self.cart:
            from .shopping import ShoppingCart
            self.cart = ShoppingCart(self)
        self.cart.add_item(candy, quantity)

    def checkout(self, payment_method: str):
        """Convert shopping cart into an order."""
        if not self.cart:
            raise ValueError("Cart is empty")
        order = self.cart.create_order(payment_method)
        self.orders.append(order)
        self.cart.clear()
        return order


class Staff(User):
    """Represents store employees — inherits from User."""
    
    def __init__(self, user_id: int, name: str, email: str, password: str, position: str):
        super().__init__(user_id, name, email, password)
        self.position = position

    def update_inventory(self, candy: "Candy", new_quantity: int):
        """Update the quantity of a candy in inventory."""
        candy.quantity = new_quantity

    def view_sales_report(self, orders: List["Order"]):
        """Generate a sales report from a list of orders."""
        total = sum(order.total_amount for order in orders)
        return f"Total sales: ${total:.2f}"
