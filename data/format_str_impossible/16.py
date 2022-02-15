def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  str1_reversed = ''.join(reversed(str1))
  str2_reversed = ''.join(reversed(str2))
  str_impossible = str1_reversed[0::2] + str2_reversed[1::2]
  str_impossible = ''.join(reversed(str_impossible))
  return ''.join(['c' for _ in range(len(str_impossible))])


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""