def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  if len(lst1) < len(lst2):
    lst1, lst2 = lst2, lst1
  lst1 = [x.lower() if type(x) == str else x for x in lst1]
  lst2 = [x.lower() if type(x) == str else x for x in lst2]
  lst1 = sorted(lst1)
  lst2 = sorted(lst2)
  lst1 = [x.upper() if type(x) ==
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   ERROR
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""