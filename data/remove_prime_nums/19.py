def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  lst3 = lst1 + lst2
  for i in lst3:
    if i in lst1 and i in lst2:
      lst1.remove(i)
      lst2.remove(i)
  return lst1, lst2


"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [4, 5, 6])   --->   FAILED
input: ([4, 6, 8], [10, 12, 14])   --->   FAILED
input: ([1, 1, 1], [37, 39, 13])   --->   FAILED
input: ([], [1, 2, 3])   --->   FAILED
"""