def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  lst1 = sorted(lst1)
  lst2 = sorted(lst2)

  combined = []

  while lst1 or lst2:
    if not lst1:
      combined.append(lst2.pop(0))
    elif not lst2:
      combined.append(lst1.pop(0))
    elif ord(lst1[0]) < ord(lst2[0]):
      combined.append(lst1.pop(0))
    else:
      combined
"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""