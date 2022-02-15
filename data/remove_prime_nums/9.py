def remove_prime_nums(lst1, lst2):
  """
  Removes the prime numbers from a combined list of two given lists
  """
  
  for i in lst2:
    # check if the number is a prime number
    if i in lst1:
      # if the number is a prime number, remove it from the larger list
      lst1.remove(i)
  return lst1


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [4, 5, 6])   --->   FAILED
input: ([4, 6, 8], [10, 12, 14])   --->   FAILED
input: ([1, 1, 1], [37, 39, 13])   --->   FAILED
input: ([], [1, 2, 3])   --->   FAILED
"""