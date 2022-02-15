def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if not lst1 or not lst2:
    return lst1 or lst2
  interweaved = [lst1[0]]
  for i, el in enumerate(lst1[1:]):
    interweaved.append(lst2[i])
    interweaved.append(el)
  interweaved.append(lst2[-1])
  return interweaved



"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [10, 12, 14])   --->   PASSED
input: (['hello'], [37, 39, 13])   --->   FAILED
input: (['hello', 5, '6'], [1, 2, 3])   --->   PASSED
"""