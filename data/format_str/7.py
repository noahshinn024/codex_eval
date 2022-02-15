def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  length = len(str1) + len(str2)
  if length % 2 == 0:
    half_length = length / 2
  else:
    half_length = (length + 1) / 2

  first_str = str1[:half_length]
  second_str = str2[:half_length]

  return first_str + second_str[::-1]


# Test cases

"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   ERROR
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""