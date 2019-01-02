def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else: evens = 0
    
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    
    if evens == 0:
        return False
    else:
        return evens % 2 ==0

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One number"
assert even_number_of_evens([2,4]) == True, "Two even numbers"
assert even_number_of_evens([3,4]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "multiple numbers, 3 even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "multiple numbers, 4 even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print ("All tests passed")