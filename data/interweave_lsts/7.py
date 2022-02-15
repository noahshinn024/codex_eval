def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if not lst1 or not lst2:
    return lst1 or lst2
  new_lst = []
  for i in range(len(lst1) + len(lst2)):
    if i % 2 == 0:
      new_lst.append(lst1[int(i/2)])
    else:
      new_lst.append(lst2[int(i/2)])
  return new_lst


"""
input: ([], [])   --->   PASSED
input: ([1, 2, 3], [])   --->   PASSED
input: ([], [10, 12, 14])   --->   PASSED
input: (['hello'], [37, 39, 13])   --->   ERROR
input: (['hello', 5, '6'], [1, 2, 3])   --->   PASSED
"""