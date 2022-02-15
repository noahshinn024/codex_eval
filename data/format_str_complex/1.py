def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  str1_reverse = str1[::-1]
  str2_reverse = str2[::-1]
  str_combined = str1_reverse + str2_reverse
  str_vowels = ""
  for i in range(len(str_combined)):
    if str_combined[i] in "aeiouAEIOU":
      str_vowels += str_combined[i]
  str_vowels = str_vowels[::-1]
  return str_vowels


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""