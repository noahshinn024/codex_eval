def format_str(str1, str2):
  """
  Reverses and deletes every other letter from a combination of two strings
  """
  
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  
  if len(str1) < len(str2):
    str1, str2 = str2, str1
  
  new_str = ""
  for i in range(len(str2)):
    if i % 2 == 0:
      new_str += str2[i]
    else:
      new_str += str1[i]
  
  new_str += str1[(i+1):]
  return new_str


"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""