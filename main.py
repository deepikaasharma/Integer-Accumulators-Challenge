"""Write the logic needed to loop through num_list and accumulate the results of multiplying each number in an accumulator variable called prod. Careful on this one: take care in initializing your accumulator variable!"""


# Leave this line alone
num_list = [6, 9, 10, 8, 7, 5]

prod = 1

# Write your code here
for i, num in enumerate(num_list):
  prod *= num

print(prod)

print(6*9*10*8*7*5)


"""Integer Accumulators Challenge 2

Initialize an accumulator named result with the value 1000 and subtract the sum of the values in num_list."""

# Leave this line alone
# num_list = [50, 9, 21, 35, 50, 10, 25, 48, 16, 48, 35, 15, 3, 9, 16, 12, 42, 14, 18, 36]

# # Write your code here
# result = 1000

# for val in num_list:
#   result = result - val


# print(result)

# print(50+9+21+35+50+ 10+25+ 48+ 16+ 48+ 35+ 15+ 3+ 9+ 16+ 12+ 42+ 14+ 18+ 36)


"""Sum up only the odd integers from mixed_data using an accumulator variable called odd_sum."""

# # Leave this line alone
# mixed_data = [50, 9, 21, "hello", 16, 48, False, 35, 15, 3, "oops am I in your way?", 9, 16, 12, 42, 3.67, 14, 18, 36]

# # Write your code here
# odd_sum = 0

# for num in mixed_data:
#   if isinstance(num, int):
#     if num%2 !=0:
#       odd_sum +=num

# print(odd_sum)