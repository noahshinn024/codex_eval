def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  if not lst1 or not lst2:
    return lst1 + lst2

  lst1_type, lst2_type = type(lst1[0]), type(lst2[0])
  lst1, lst2 = sorted(lst1), sorted(lst2)
  lst1 = [lst1_type(x) for x in lst1]
  lst2 = [lst2_type(x) for x in lst2]

  return lst1 + lst
"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""