def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  if type(str1) != str or type(str2) != str:
    raise TypeError
  if len(str1) != len(str2):
    raise ValueError
  vowels = 'aeiou'
  result = ''
  result += ''.join([str2[i] for i in range(len(str2)) if str1[i] in vowels])
  result += ''.join([str1[i] for i in range(len(str1)) if str2[i] in vowels])
  return result[::-1]
"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""