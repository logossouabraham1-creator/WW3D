# def recursive_sum(example):
#     if len(example) == 1:
#         return example[0]
#     return example[0] + recursive_sum(example[1:])
# print(recursive_sum([1,2,3,4,5]))

# def count_greater_than_10(example):
#     if len(example) == 0 :
#         return 0 

#     result = count_greater_than_10(example[1:])
#     if example[0] > 10:
#         return 1 + result 
#     else :
#         return result

# print(count_greater_than_10([10,20,30]))

# def contains(numbers, target):
#     if len(numbers) == 0:
#         return False
#     if numbers[0] == target :
#         return True
#     return contains(numbers[1:],target)
# print(contains([4, 8, 12, 20,15], 15))


# def count_digits(n):
#     if n == 0 :
#         return 0
#     result = count_digits(n//10)
#     return 1 + result 
# result = 58
# digits = count_digits(result)
# current_digits = 7 
# print(current_digits * (10**digits) + result)

# def count_digits(n):
#     if n == 0:
#         return 0

#     return 1 + count_digits(n // 10)


# def reverse_number(n):
    # Base case: a single digit is already reversed
#     if n < 10:
#         return n
#     current_digit = n % 10
#     result = reverse_number(n // 10)
#     digits = count_digits(result)
#     return current_digit * (10 ** digits) + result
# print(reverse_number(1234))
