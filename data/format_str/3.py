def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  new_str = ''
  for i in range(len(str1)):
    if i % 2 == 0:
      new_str += str1[i]
    else:
      new_str += str2[i]
  return new_str
"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""