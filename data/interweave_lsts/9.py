def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if len(lst1) == 0 or len(lst2) == 0:
    raise ValueError('Lists must be non-empty')
  new_list = []
  while len(lst1) > 0 and len(lst2) > 0:
    new_list.append(lst1.pop(0))
    new_list.append(lst2.pop(0))
  if len(lst1) > 0:
    new_list.extend(lst1)
  elif len(lst
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [10, 12, 14])   --->   ERROR
input: (['hello'], [37, 39, 13])   --->   ERROR
input: (['hello', 5, '6'], [1, 2, 3])   --->   ERROR
"""