def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  
  # Convert inputs to strings if they are not already
  if type(lst1) is not str:
    lst1 = str(lst1)
  if type(lst2) is not str:
    lst2 = str(lst2)
  # Combine lists into a single list
  lst = lst1 + lst2
  # Sort combined list
  lst = sorted(lst)
  # Split list back into two lists
  lst1 = lst[:len(lst1)]
  lst
"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [1, 9, 3])   --->   FAILED
input: (['a', 1], ['b', 'c', 'a'])   --->   FAILED
input: (['z', '?', '6'], [1, 2, 3])   --->   FAILED
"""