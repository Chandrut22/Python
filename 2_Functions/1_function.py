# --- 1. Define the function with a parameter and a return value ---
def calculate_stats(numbers_list):
    """
    Calculates the sum, average, max, and min for a list of numbers.
    Returns the results in a dictionary.
    """
    # Handle empty lists to avoid errors
    if not numbers_list:
        return None # Return None if the list is empty

    total_sum = sum(numbers_list)
    count = len(numbers_list)
    average = total_sum / count
    maximum = max(numbers_list)
    minimum = min(numbers_list)
    
    # Return a dictionary containing all the results
    return {
        "sum": total_sum,
        "average": average,
        "max": maximum,
        "min": minimum
    }

# --- 2. Call the function and use its output ---
scores = [88, 95, 72, 100, 85, 72]
stats = calculate_stats(scores)

# The 'stats' variable now holds the dictionary returned by the function
if stats is not None:
    print(f"Analyzing the scores: {scores}")
    print(f"Sum of scores: {stats['sum']}")
    print(f"Average score: {stats['average']:.2f}") # Format to 2 decimal places
    print(f"Highest score: {stats['max']}")
    print(f"Lowest score: {stats['min']}")

# Example with an empty list
empty_stats = calculate_stats([])
print(f"\nResult for an empty list: {empty_stats}")