def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  return "".join(vowels[::-1]) + "".join(consonants[::-2])

# Test Cases
str1 = "abc
"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   ERROR
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""