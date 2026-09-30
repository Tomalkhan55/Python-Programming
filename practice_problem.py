# python programming practive problem

# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("number is odd")


# 2.Write a Python program to count the number 4 in a given list.

# lists = [12, 2, 3, 4, 5, 69]


# def list_count_4(lists):
#     for list in lists:
#         if list == 4:
#             print("the number 4 is found the list.")

# list_count_4(lists)


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

# print(is_vowel('c'))
# print(is_vowel('i'))


# names = "My name is tomal khan"
# for name in names:
    # print(name)


# def concatenate_list_Data(list):
#     result = ''

#     for element in list:
#         result += str(element)

#     return result


# print(concatenate_list_Data([1, 5, 12, 2]))


# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]

# for number in numbers:
#     if number == 237:
#         print(number)
#         break
#     elif number % 2 == 0:
#         print(number)


# Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.

# string_maps = {
#     "1": "abc",
#     "2": "def",
#     "3": "ghi",
#     "4": "jkl",
#     "5": "mno",
#     "6": "pqrs",
#     "7": "tuv",
#     "8": "wxy",
#     "9": "z"
# }

# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.


# def check_list(numbers):
#     if numbers.count(19) == 2 and numbers.count(5) >= 3:
#         return True
#     else:
#         return False


# def test(nums):
#     return nums.count(19) == 2 and nums.count(5) >= 3


# numbers = [19, 19, 15, 5, 3, 5, 5, 2];
# # numbers = [19, 1k5, 15, 5, 3, 3, 5, 2]
# print(test(numbers))

def check_list(numbers):
    if len(numbers) == 8 and numbers.count(numbers[4]) == 3:
        return True
    else:
        return False
    
numbers = [19, 19, 15, 5, 5, 5, 1, 2]

print(check_list(numbers))





