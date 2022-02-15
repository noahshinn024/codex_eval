def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if not lst1:
    return lst2
  if not lst2:
    return lst1
  if len(lst1) == 1:
    if len(lst2) == 1:
      return [lst1[0], lst2[0]]
    else:
      return [lst1[0]] + lst2
  if len(lst2) == 1:
    return [lst2[0]] + lst1
  return [lst1[0], lst2[0]]
"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [10, 12, 14])   --->   PASSED
input: (['hello'], [37, 39, 13])   --->   PASSED
input: (['hello', 5, '6'], [1, 2, 3])   --->   FAILED
"""