def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  output = ""

  for i in range(len(str1)):
    output += str1[i] + str2[i]

  return output


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""