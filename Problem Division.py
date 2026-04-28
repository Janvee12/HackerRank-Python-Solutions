# Problem: Division
# Platform: HackerRank
# Approach: Take two integers and print integer division and float division
# Time Complexity: O(1)
# Space Complexity: O(1)

if __name__ == '__main__':
    
    # Step 1: Take input values
    a = int(input())
    b = int(input())
    
    # Step 2: Perform division operations
    
    # Integer division (floor division) → removes decimal part
    print(a // b)
    
    # Float division → gives exact result with decimal
    print(a / b)