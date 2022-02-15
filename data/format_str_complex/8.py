def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str_comb = str1 + str2
  vowels = 'aeiou'
  new_str = ''
  for i in range(0, len(str_comb)):
    if i % 2 == 0:
      new_str += str_comb[i]
  return new_str[::-1]


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""