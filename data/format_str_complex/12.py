def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  return str2[::-1].replace('a', '', len(str2)//2)[::-1]


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""