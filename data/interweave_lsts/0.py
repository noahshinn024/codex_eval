def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if len(lst1) != len(lst2):
    raise ValueError("Lists must be the same length")
  ret = []
  for l1, l2 in zip(lst1, lst2):
    ret.extend([l1, l2])
  return ret


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [10, 12, 14])   --->   ERROR
input: (['hello'], [37, 39, 13])   --->   ERROR
input: (['hello', 5, '6'], [1, 2, 3])   --->   PASSED
"""