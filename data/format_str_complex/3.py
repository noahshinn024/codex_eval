def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  str_combined = str1 + str2
  str_reversed = str_combined[::-1]
  str_vowels = ''
  for letter in str_reversed:
    if letter in 'aeiouAEIOU':
      str_vowels += letter
  return str_vowels[::-1]


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""