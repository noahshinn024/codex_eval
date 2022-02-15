def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  return [x for x in lst1 + lst2 if not is_prime(x)]
"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""