# Shiva-coder: Binary Search Algorithm
def binary_search_tool():
    # A sorted list is REQUIRED for Binary Search
    numbers = [10, 22, 35, 47, 59, 72, 88, 99]
    print(f"\nSearch Database: {numbers}")
    
    target = int(input("Enter number to find: "))
    
    low = 0
    high = len(numbers) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            print(f"🎯 Target {target} found at Index {mid}!")
            found = True
            break
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print("❌ Number not in the database.")

if __name__ == "__main__":
    binary_search_tool()
