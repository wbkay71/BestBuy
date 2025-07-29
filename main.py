import products
import store


def start(store_obj):
    """
    Display the store menu and handle user interactions.

    Args:
        store_obj: Store object containing the products
    """
    while True:
        # Display menu
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # Get user choice
        choice = input("Please choose a number: ")

        # Handle menu options
        if choice == "1":
            # List all active products
            print("\n------")
            active_products = store_obj.get_all_products()
            for product in active_products:
                print(product.show())
            print("------")

        elif choice == "2":
            # Show total quantity in store
            total = store_obj.get_total_quantity()
            print(f"\nTotal of {total} items in store")

        elif choice == "3":
            # Make an order
            shopping_list = []
            active_products = store_obj.get_all_products()

            print("\n------")
            # Show available products with numbers
            for i, product in enumerate(active_products):
                print(f"{i + 1}. {product.show()}")
            print("------")

            print("When you want to finish order, enter empty text.")

            # Get order items from user
            while True:
                # Ask which product
                product_num = input("Which product # do you want? ")

                # Empty input means finish order
                if product_num == "":
                    break

                # Validate product number
                try:
                    product_index = int(product_num) - 1
                    if product_index < 0 or product_index >= len(active_products):
                        print("Invalid product number!")
                        continue
                except ValueError:
                    print("Please enter a valid number!")
                    continue

                # Ask for quantity
                quantity_str = input("What amount do you want? ")

                # Validate quantity
                try:
                    quantity = int(quantity_str)
                    if quantity <= 0:
                        print("Amount must be positive!")
                        continue
                except ValueError:
                    print("Please enter a valid number!")
                    continue

                # Add to shopping list
                product = active_products[product_index]
                shopping_list.append((product, quantity))
                print("Product added to list!")

            # Process the order if shopping list is not empty
            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"\nOrder made! Total payment: ${total_price}")
                except Exception as error:
                    print(f"\nError while making order: {error}")
            else:
                print("\nNo items ordered.")

        elif choice == "4":
            # Quit the program
            print("\nThank you for visiting Best Buy!")
            break

        else:
            print("\nInvalid choice! Please enter 1-4.")


def main():
    """
    Main function to set up the store and start the interface.
    """
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    # Create store
    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()
