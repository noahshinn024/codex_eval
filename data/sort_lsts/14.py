def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1 = list(sorted(lst1))
  lst2 = list(sorted(lst2))
  if len(lst1) > len(lst2):
    lst1, lst2 = lst2, lst1
  c = []
  i = 0
  j = 0
  while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
      c.append(lst1[i])
     
"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""