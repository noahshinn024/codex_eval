def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  

  if len(str1) > len(str2):
    str1, str2 = str2, str1

  str1 = str1[::-1]
  str2 = str2[::-1]
  new_string = ""

  for i in range(len(str1)):
    new_string += str1[i]
    try:
      new_string += str2[i]
    except:
      continue

  return new_string
"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""