class Product:
    """
    Represents a product in the store with name, price, quantity and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new product.

        Args:
            name (str): Product name
            price (float): Product price
            quantity (int): Initial quantity in stock

        Raises:
            Exception: If name is empty or price/quantity are negative
        """
        # Validate inputs before creating the product
        if not name:
            raise Exception("Product name cannot be empty")
        if price < 0:
            raise Exception("Product price cannot be negative")
        if quantity < 0:
            raise Exception("Product quantity cannot be negative")

        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Products are active by default

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.

        Returns:
            int: Current quantity in stock
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product.
        If quantity reaches 0, deactivate the product.

        Args:
            quantity (int): New quantity value
        """
        self.quantity = quantity
        # Automatically deactivate if no stock left
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check if the product is active.

        Returns:
            bool: True if active, False otherwise
        """
        return self.active

    def activate(self):
        """
        Activate the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False

    def show(self):
        """
        Print a string representation of the product.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Buy a given quantity of the product.

        Args:
            quantity (int): Amount to buy

        Returns:
            float: Total price of the purchase

        Raises:
            Exception: If product is inactive or insufficient quantity
        """
        # Check if product is active
        if not self.active:
            raise Exception("Product is not active")

        # Check if we have enough quantity
        if quantity > self.quantity:
            raise Exception("Insufficient quantity in stock")

        # Check for invalid quantity
        if quantity <= 0:
            raise Exception("Purchase quantity must be positive")

        # Calculate total price
        total_price = self.price * quantity

        # Update quantity (using setter to handle deactivation)
        self.set_quantity(self.quantity - quantity)

        return total_price


# Test code - uncomment to test the class
if __name__ == "__main__":
    # Create products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # Test buying
    print(bose.buy(50))  # Should print: 12500.0
    print(mac.buy(100))  # Should print: 145000.0
    print(mac.is_active())  # Should print: False (because quantity is now 0)

    # Show products
    bose.show()  # Bose QuietComfort Earbuds, Price: 250, Quantity: 450
    mac.show()  # MacBook Air M2, Price: 1450, Quantity: 0

    # Update quantity
    bose.set_quantity(1000)
    bose.show()  # Bose QuietComfort Earbuds, Price: 250, Quantity: 1000
