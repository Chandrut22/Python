def process_order(order_id, *items, **customer_details):
    """Processes a customer order."""
    print(f"--- Processing Order #{order_id} ---")
    
    # *items is a tuple
    print("Items Ordered:")
    for item in items:
        print(f"- {item}")
        
    # **customer_details is a dictionary
    print("\nCustomer Details:")
    for key, value in customer_details.items():
        print(f"- {key.title()}: {value}")

# Call the function with a mix of argument types
process_order(
    101,                           # Standard argument
    "Laptop", "Mouse", "Keyboard", # These become *args
    name="Anil Kumar",             # These become **kwargs
    delivery_date="2025-10-22"
)