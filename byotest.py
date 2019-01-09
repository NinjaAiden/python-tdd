def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
# test fails    
#test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)

# test passes
#test_are_equal(8, 8)

# test fails
#test_not_equal(5, 5)

# test passes
#test_not_equal(5, 7)

# test fails
#test_is_in([1, 2, 3, 4, 5], 6)

# test passes
test_is_in([1, 2, 3, 4, 5], 3)

print("tests passed")