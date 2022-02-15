def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  # make new list to contain the prime numbers
  prime_numbers = []
  # append the numbers to the prime_numbers list
  for x in lst1:
    prime_numbers.append(x)
  for x in lst2:
    prime_numbers.append(x)
  # remove the prime numbers from the combined list
  prime_numbers = remove_duplicates(prime_numbers)
  prime_numbers.sort()
  for y in prime_numbers:
    if is_prime(y
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""