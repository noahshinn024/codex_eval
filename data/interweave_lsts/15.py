def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if len(lst1) == 1:
    return lst1 + lst2
  else:
    return [lst1[0]] + interweave_lsts(lst2, lst1[1:])

# 4.2

"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [10, 12, 14])   --->   ERROR
input: (['hello'], [37, 39, 13])   --->   PASSED
input: (['hello', 5, '6'], [1, 2, 3])   --->   ERROR
"""