def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  lst3 = lst1 + lst2
  lst_prime_nums = []
  for i in lst3:
    if is_prime(i) == True:
      lst_prime_nums.append(i)
  for i in lst_prime_nums:
    lst3.remove(i)
  return lst3

# 
"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""