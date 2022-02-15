def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  vowels = "aeiou"
  str1 = str1[::-1]
  str2 = str2[::-1]
  new_str = ""
  for i in range(len(str1)):
    if i % 2 == 0:
      new_str += str1[i]
    else:
      new_str += str2[i]
  return "".join([c for c in new_str if c in vowels][::-1])


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""