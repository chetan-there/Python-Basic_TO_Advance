# A List is an ordered, mutable collection.

numbers = [10, 20, 30, 40]

print(numbers[0])   # access element
print(numbers[-1])  # last element

nums = [1,2,3]

nums.append(4)      # add element
nums.insert(1,10)   # insert at index
nums.remove(2)      # remove element
nums.pop()          # remove last
nums.sort()         # sort list

# A Tuple is an ordered but immutable collection.
"""
Faster than lists

Memory efficient

Used for fixed data
"""
point = (10, 20)

print(point[0])

# A Set stores unique elements only.

"""
Properties
    No duplicates
    Unordered
    Fast lookup
"""

numbers = {1,2,3,4}

numbers.add(5)
numbers.remove(2)

# Dictionary stores key → value pairs.

student = {
    "name": "Chetan",
    "age": 22
}

print(student["name"])

student.keys()
student.values()
student.items()
student.get("name")