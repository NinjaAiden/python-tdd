def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "1 Upper case"
assert count_upper_case("a") == 0, "no upper case"
assert count_upper_case("£$%^&") == 0, "special characters"
assert count_upper_case("Hello^") == 1, "one uppercase"
assert count_upper_case("HeLlO") == 3, "3 uppercase"

print("All tests passed")