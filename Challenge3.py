def highest_consonant_value(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0
    
    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    return max(max_value, current_value)

print(highest_consonant_value("frank"))  
