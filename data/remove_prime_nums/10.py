def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  prime_nums = get_prime_nums(max(lst1 + lst2))
  for num in prime_nums:
    while num in lst1: lst1.remove(num)
    while num in lst2: lst2.remove(num)
  return lst1, lst2


"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [4, 5, 6])   --->   ERROR
input: ([4, 6, 8], [10, 12, 14])   --->   ERROR
input: ([1, 1, 1], [37, 39, 13])   --->   ERROR
input: ([], [1, 2, 3])   --->   ERROR
"""