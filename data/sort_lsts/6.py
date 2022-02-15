def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  

  lst1 = lst1.split()
  lst2 = lst2.split()

  lst = lst1 + lst2

  lst = sorted(lst)

  # 
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   ERROR
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""