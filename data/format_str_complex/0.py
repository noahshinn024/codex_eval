def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str3 = str1 + str2
  str4 = ''
  for index in range(len(str3)):
    if index % 2 == 0:
      str4 += str3[index]
  str5 = ''
  for char in str4:
    if char in 'aeiou':
      str5 += char
  str5 = str5[::-1]
  return str5


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""