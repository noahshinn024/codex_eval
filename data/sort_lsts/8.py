def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  
  if len(lst1) == 0 or len(lst2) == 0:
    return [lst1, lst2]
  
  lst1 = list(lst1)
  lst2 = list(lst2)
  
  # If one of the lists is empty, make the other the only list 
  if len(lst1) == 0:
    return [lst2]
  elif len(lst2) == 0:
    return [lst1]
  
  # Split
"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   FAILED
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""