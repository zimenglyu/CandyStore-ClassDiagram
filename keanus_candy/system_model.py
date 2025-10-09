# Main system model - imports all classes for easy access
from .models.person import Person, User, Staff
from .models.product import Product, Candy, Catalog
from .models.shopping import CartItem, ShoppingCart, Order, OrderItem
from .models.payment import PaymentMethod, CreditCard, PayPal
