def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  lst1 += lst2
  return lst1


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [10, 12, 14])   --->   PASSED
input: (['hello'], [37, 39, 13])   --->   PASSED
input: (['hello', 5, '6'], [1, 2, 3])   --->   FAILED
"""