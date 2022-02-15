def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if len(lst1) == len(lst2) == 0: return []
  if len(lst1) == len(lst2) == 1: return [lst1[0]] + [lst2[0]]
  return [lst1[0]] + [lst2[0]] + interweave_lsts(lst1[1:], lst2[1:])


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [10, 12, 14])   --->   ERROR
input: (['hello'], [37, 39, 13])   --->   ERROR
input: (['hello', 5, '6'], [1, 2, 3])   --->   ERROR
"""