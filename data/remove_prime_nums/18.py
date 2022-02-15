def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  for i in lst1:
    if is_prime(i) == True:
      lst1.remove(i)
  for i in lst2:
    if is_prime(i) == True:
      lst2.remove(i)
  return lst1, lst2



"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""