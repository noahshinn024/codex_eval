def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  assert len(lst1) == len(lst2)
  res = []
  for i in range(0, len(lst1)):
    if type(lst1[i]) == str:
      res.append(lst1[i])
      res.append(lst2[i])
    else:
      res.append(lst2[i])
      res.append(lst1[i])
  return res


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   ERROR
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""