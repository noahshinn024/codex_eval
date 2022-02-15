def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  lst1_len = len(lst1)
  lst2_len = len(lst2)

  lst1_idx = 0
  lst2_idx = 0
  lst3 = []
  while lst1_idx < lst1_len and lst2_idx < lst2_len:
    lst3.append(lst1[lst1_idx])
    lst1_idx += 1
    lst3.append(lst2[lst2
"""
input: ([], [])   --->   ERROR
input: ([1, 2, 3], [])   --->   ERROR
input: ([], [10, 12, 14])   --->   ERROR
input: (['hello'], [37, 39, 13])   --->   ERROR
input: (['hello', 5, '6'], [1, 2, 3])   --->   ERROR
"""