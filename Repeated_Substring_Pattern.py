def repeatedSubstringPattern(s: str) -> bool:
    # Get the length of the string
    n = len(s)
    
    # Check all possible substring lengths that can divide the string evenly
    for length in range(1, n // 2 + 1):
        # If length doesn't divide string evenly, skip
        if n % length != 0:
            continue
            
        # Get the substring pattern
        pattern = s[:length]
        
        # Check if repeating this pattern length times creates original string
        if pattern * (n // length) == s:
            return True
            
    return False