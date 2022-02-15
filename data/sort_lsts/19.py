def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1.sort()
  lst2.sort()
  lst3 = []
  for i in range(len(lst1)):
    lst3.append(lst1[i])
    lst3.append(lst2[i])
  return lst3


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""