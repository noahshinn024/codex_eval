def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  return str2[::-1][::2] + str1[::2]


# Uncomment these function calls to test your  function:

"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""