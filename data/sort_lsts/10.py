def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1_sorted = sorted(lst1)
  lst2_sorted = sorted(lst2)
  lst_sorted = []
  for i in range(len(lst1_sorted)):
    lst_sorted.append(lst1_sorted[i])
    lst_sorted.append(lst2_sorted[i])
  return lst_sorted
"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""