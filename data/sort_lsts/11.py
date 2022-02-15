def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  if type(lst1[0]) == str:
    return ''.join(sorted(lst1 + lst2))
  return sorted(lst1 + lst2)


"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [1, 9, 3])   --->   ERROR
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""