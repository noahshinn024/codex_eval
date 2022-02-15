def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  lst3 = lst1 + lst2
  lst3 = [x for x in lst3 if x not in PRIMES]
  return lst3


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""