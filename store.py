import products


class Store:
    """
    Represents a store that manages multiple products.
    Uses composition to hold a list of Product objects.
    """

    def __init__(self, product_list):
        """
        Initialize a new store with a list of products.

        Args:
            product_list: List of Product objects
        """
        self.products = product_list

    def add_product(self, product):
        """
        Add a new product to the store.

        Args:
            product: Product object to add
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.

        Args:
            product: Product object to remove
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Get the total quantity of all products in the store.

        Returns:
            int: Sum of quantities of all products
        """
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """
        Get all active products in the store.

        Returns:
            List[Product]: List of active products only
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Process an order for multiple products.

        Args:
            shopping_list: List of tuples (product, quantity)

        Returns:
            float: Total price of the order

        Raises:
            Exception: If any product purchase fails
        """
        total_price = 0.0

        # Process each item in the shopping list
        for product, quantity in shopping_list:
            # Buy the product and add to total
            # The buy method will raise exception if something goes wrong
            price = product.buy(quantity)
            total_price += price

        return total_price


# Test code
if __name__ == "__main__":
    # Create product list
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Create store
    best_buy = Store(product_list)

    # Get all products
    all_products = best_buy.get_all_products()

    # Test total quantity
    print(best_buy.get_total_quantity())  # Should print: 850 (100 + 500 + 250)

    # Test ordering
    order_price = best_buy.order([(all_products[0], 1), (all_products[1], 2)])
    print(order_price)  # Should print: 1950.0 (1450 + 500)