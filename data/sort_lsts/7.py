def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  ret = []
  for i in range(len(lst1)):
    if isinstance(lst1[i], int):
      ret.append(str(lst1[i]) + str(lst2[i]))
    else:
      ret.append(str(lst2[i]) + str(lst1[i]))
  return ret


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   FAILED
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""