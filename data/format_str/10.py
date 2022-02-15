def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  return str1[::-1] + str2[::2]


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""