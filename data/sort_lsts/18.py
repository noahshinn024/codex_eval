def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1 = [str(x) for x in lst1]
  lst2 = [str(x) for x in lst2]
  lst1.sort()
  lst2.sort()
  return [x for x in lst1] + [x for x in lst2]


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   FAILED
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""