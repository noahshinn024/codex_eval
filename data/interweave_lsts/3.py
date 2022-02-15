def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  return [val for pair in zip(lst1, lst2) for val in pair]


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [10, 12, 14])   --->   FAILED
input: (['hello'], [37, 39, 13])   --->   FAILED
input: (['hello', 5, '6'], [1, 2, 3])   --->   PASSED
"""