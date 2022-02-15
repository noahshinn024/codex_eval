def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  

  new_lst = []
  for x in lst1:
    if x not in lst2:
      new_lst.append(x)

  return new_lst



"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [4, 5, 6])   --->   FAILED
input: ([4, 6, 8], [10, 12, 14])   --->   FAILED
input: ([1, 1, 1], [37, 39, 13])   --->   FAILED
input: ([], [1, 2, 3])   --->   FAILED
"""