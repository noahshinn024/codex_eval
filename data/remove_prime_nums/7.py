def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  for num in lst1:
    if is_prime(num):
      lst1.remove(num)
  for num in lst2:
    if is_prime(num):
      lst2.remove(num)
  return lst1, lst2


"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""