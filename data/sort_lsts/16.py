def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  return sorted(lst1 + lst2, key=str)

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [1, 9, 3])   --->   PASSED
input: (['a', 1], ['b', 'c', 'a'])   --->   PASSED
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""