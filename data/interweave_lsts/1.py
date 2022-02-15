def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if len(lst1) == 0:
    return lst2
  if len(lst2) == 0:
    return lst1
  return [lst1[0]] + interweave_lsts(lst2, lst1[1:])


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [10, 12, 14])   --->   PASSED
input: (['hello'], [37, 39, 13])   --->   ERROR
input: (['hello', 5, '6'], [1, 2, 3])   --->   ERROR
"""