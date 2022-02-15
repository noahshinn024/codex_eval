def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1 = sorted(lst1)
  lst2 = sorted(lst2)
  lst3 = []
  i = 0
  j = 0
  while i < len(lst1) or j < len(lst2):
    if i == len(lst1):
      lst3.append(lst2[j])
      j += 1
    elif j == len(lst2):
      lst3.append(lst1[i])
      i += 1
    elif chr
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   ERROR
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""