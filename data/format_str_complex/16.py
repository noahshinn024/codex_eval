def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  str3 = str2[::-1]
  str4 = str1 + str3
  str5 = str4[::2]
  str6 = ''
  for char in str5:
    if char in 'aeiou':
      str6 += char
  str7 = str6[::-1]
  return str7

# 
"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""