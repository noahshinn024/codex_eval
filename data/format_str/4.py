def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  new_str = str1[::-1]
  new_str2 = str2[::2]
  return new_str + new_str2

str1 = "abc
"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   ERROR
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""