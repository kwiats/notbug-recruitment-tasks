"""
1. Create good script to create new list, which only contains users from Poland. Try to do it
with List Comprehension.
users = [{"name": "Kamil", "country":"Poland"}, {"name":"John", "country": "USA"}, {"name":
"Yeti"}]
2. Display sum of first ten elements starting from element 5:
numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]
3. Fill list with powers of 2, n [1..20] """

# 1

from typing import List


def get_user_from(from_country: str, users: List) -> List:
    return [user for user in users if user.get("country") == from_country]


users = [
    {"name": "Kamil", "country": "Poland"},
    {"name": "John", "country": "USA"},
    {"name": "Yeti"},
]
new_list = get_user_from("Poland", users)

print(new_list)

# 2


def get_sum(numbers: list, from_index: int, to_index: int) -> int:
    return sum(numbers[from_index:to_index])


numbers = [
    1,
    5,
    2,
    3,
    1,
    4,
    1,
    23,
    12,
    2,
    3,
    1,
    2,
    31,
    23,
    1,
    2,
    3,
    1,
    23,
    1,
    2,
    3,
    123,
]

from_index = 5
to_index = from_index + 10

number = get_sum(numbers, from_index, to_index)

print(number)

# 3


def get_power_of_2(n: int) -> List:
    return [x * 2 for x in range(n)]


lst = get_power_of_2(19)
print(lst)
