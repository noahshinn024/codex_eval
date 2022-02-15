def interweave_lsts(lst1, lst2):
  """
  Interweaves two lists starting with the first list
  """
  
  if len(lst1) > len(lst2):
    big_lst = lst1
    sml_lst = lst2
  else:
    big_lst = lst2
    sml_lst = lst1
  interwoven_lst = []
  small_lst_idx = 0
  for big_lst_idx in range(len(big_lst)):
    interwoven_lst.append(big_lst[big_lst_idx])
"""
input: ([], [])   --->   FAILED
input: ([1, 2, 3], [])   --->   FAILED
input: ([], [10, 12, 14])   --->   FAILED
input: (['hello'], [37, 39, 13])   --->   FAILED
input: (['hello', 5, '6'], [1, 2, 3])   --->   FAILED
"""