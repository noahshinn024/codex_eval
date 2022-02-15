def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1 = list(lst1)
  lst2 = list(lst2)
  lst1.sort()
  lst2.sort()
  lst = lst1 + lst2
  return lst
"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [1, 9, 3])   --->   PASSED
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""