def sort_lsts(lst1, lst2):
  """
  Combines the two given lists after they are sorted according to
  the ascii table. Inputs may be strings or integers. Types should
  be preserved in the output list
  """
  

  # If the lists are empty, return an empty list
  if len(lst1) == 0:
    return []
  elif len(lst2) == 0:
    return []

  # Base case: If either list is length 1, return the other
  elif len(lst1) == 1:
    return lst1 + lst2
  elif len(lst2) == 1:
    return lst2 + lst1

  # Recursive case
  else:
    # Find the middle index of each list
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [1, 9, 3])   --->   ERROR
input: (['a', 1], ['b', 'c', 'a'])   --->   ERROR
input: (['z', '?', '6'], [1, 2, 3])   --->   ERROR
"""