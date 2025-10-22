# --- Using a regular function (def) ---
def add_regular(x, y):
    return x + y

# --- Using a lambda function ---
# lambda arguments: expression
add_lambda = lambda x, y: x + y

# Calling both functions
result_regular = add_regular(5, 3)
result_lambda = add_lambda(5, 3)

print(f"Result from regular function: {result_regular}")
print(f"Result from lambda function: {result_lambda}")
print(f"The results are the same: {result_regular == result_lambda}")


# A list of dictionaries representing products
products = [
    {"name": "Laptop", "price": 80000},
    {"name": "Mouse", "price": 1500},
    {"name": "Keyboard", "price": 3000},
]

# --- Sorting by name (default alphabetical) ---
sorted_by_name = sorted(products, key=lambda item: item["name"])
print("--- Sorted by Name ---")
for product in sorted_by_name:
    print(product)

# --- Sorting by price using a lambda function ---
# The 'key' argument tells sorted() HOW to sort.
# Our lambda function takes an item and returns its price.
# sorted() then uses this price for the comparison.
sorted_by_price = sorted(products, key=lambda item: item["price"])

print("\n--- Sorted by Price ---")
for product in sorted_by_price:
    print(product)