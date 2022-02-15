def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  str1_rev = str1[::-1]
  str2_rev = str2[::-1]
  str_fin = ""
  for i in range(len(str1)):
    if i%2 == 0:
      str_fin += str1_rev[i] + str2_rev[i]
    else:
      str_fin += str2_rev[i] + str1_rev[i]
  return str_fin


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""